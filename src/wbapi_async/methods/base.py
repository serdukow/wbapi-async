from __future__ import annotations

from abc import ABC, abstractmethod
from functools import reduce
from typing import TYPE_CHECKING, Any, ClassVar

from pydantic import BaseModel, ConfigDict, TypeAdapter

from ..types.request_limit import RequestLimit


if TYPE_CHECKING:
    from ..client.api import WbAPI
    from ..types.base import BaseType


class WbMethod(BaseModel, ABC):
    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        populate_by_name=True,
        extra="allow",
    )

    if TYPE_CHECKING:
        __return__: type[BaseType]
        __api__: ClassVar[str]
        __method__: ClassVar[str]
        __http_method__: ClassVar[str]
        # Dot-path into response.data, e.g. "data.listGoods" or "items".
        # None = deserialize entire response.data as __return__.
        __data_key__: ClassVar[str | None]
        # Full URL override — skips build_url and set_token (unofficial APIs).
        __url__: ClassVar[str | None]
        __unofficial__: ClassVar[bool]
        # Method path template with {field} placeholders, e.g. "api/v1/supplies/{supply_id}/goods".
        __method_template__: ClassVar[str | None]
    else:

        @property
        @abstractmethod
        def __return__(self) -> type:
            pass

        @property
        @abstractmethod
        def __api__(self) -> str:
            pass

        @property
        @abstractmethod
        def __method__(self) -> str:
            pass

        @property
        def __http_method__(self) -> str:
            return "GET"

        @property
        def __data_key__(self) -> str | None:
            return None

        @property
        def __url__(self) -> str | None:
            return None

        @property
        def __unofficial__(self) -> bool:
            return False

        @property
        def __method_template__(self) -> str | None:
            return None

    def _get_url(self, wb_api: WbAPI) -> str:
        if url := getattr(self, "__url__", None):
            return url
        template = getattr(self, "__method_template__", None)
        if template:
            fields = {name: getattr(self, name) for name in self.__class__.model_fields}
            method = template.format(**fields)
            return wb_api.session.build_url(self.__api__, method)
        return wb_api.session.build_url(self.__api__, self.__method__)

    def _extract(self, data: Any) -> Any:
        """Walk dot-path from __data_key__ and return the target value."""
        key: str | None = getattr(self, "__data_key__", None)
        if key is None:
            return data
        return reduce(lambda d, k: d[k], key.split("."), data)

    async def _dispatch(
        self,
        wb_api: WbAPI,
        http_method: str,
        url: str,
        params: dict[str, Any],
        limit: RequestLimit | None,
    ) -> Any:
        if http_method == "GET":
            return await wb_api.session.get(url, params=params or None, limit=limit)
        elif http_method == "POST":
            return await wb_api.session.post(url, json=params or None, limit=limit)
        elif http_method == "PUT":
            return await wb_api.session.put(url, json=params or None, limit=limit)
        elif http_method == "PATCH":
            return await wb_api.session.patch(url, json=params or None, limit=limit)
        elif http_method == "DELETE":
            return await wb_api.session.delete(url, params=params or None, limit=limit)
        else:
            raise ValueError(f"Unsupported HTTP method: {http_method}")

    async def emit(self, wb_api: WbAPI) -> Any:
        unofficial = getattr(self, "__unofficial__", False)
        if not unofficial:
            wb_api.session.headers.set_token(wb_api._token)

        url = self._get_url(wb_api)
        request_limit: RequestLimit | None = getattr(self, "request_limit", None)
        http_method = getattr(self, "__http_method__", "GET").upper()
        excluded_fields = {"request_limit"}

        # Auto-pagination: if method has limit/offset fields and limit is None,
        # fetch all pages and return a combined list.
        has_pagination = hasattr(self, "limit") and hasattr(self, "offset")
        if has_pagination and getattr(self, "limit", None) is None:
            page_size = 1000
            current_offset = 0
            result: list[Any] = []
            return_type = self.__return__

            while True:
                page_copy = self.model_copy(update={"limit": page_size, "offset": current_offset})
                params = page_copy.model_dump(
                    by_alias=True, exclude_none=True, exclude=excluded_fields
                )
                data = await self._dispatch(wb_api, http_method, url, params, request_limit)
                page = self._extract(data)
                if not isinstance(page, list) or not page:
                    break
                result.extend(TypeAdapter(list[return_type]).validate_python(page))  # type: ignore[valid-type]
                if len(page) < page_size:
                    break
                current_offset += page_size

            return result

        params = self.model_dump(by_alias=True, exclude_none=True, exclude=excluded_fields)
        data = await self._dispatch(wb_api, http_method, url, params, request_limit)

        if getattr(self, "__empty_response__", False) or data is None:
            return None

        raw = self._extract(data)

        return_type = self.__return__
        if isinstance(raw, list):
            return TypeAdapter(list[return_type]).validate_python(raw)  # type: ignore[valid-type]
        return return_type.model_validate(raw)

    def __await__(self) -> Any:
        raise RuntimeError(f"{self.__class__.__name__} cannot be called directly.")
