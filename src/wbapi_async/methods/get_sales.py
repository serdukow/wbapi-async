from __future__ import annotations

from typing import TYPE_CHECKING, Any

from pydantic import Field, TypeAdapter

from ..types.request_limit import RequestLimit
from ..types.sale import Sale
from .base import WbMethod


if TYPE_CHECKING:
    from ..client.api import WbAPI


class GetSales(WbMethod):
    """
    Returns sale and return information.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Main-Reports/paths/~1api~1v1~1supplier~1sales/get
    """

    __return__ = Sale
    __api__ = "statistics-api"
    __method__ = "api/v1/supplier/sales"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=1)

    date_from: str = Field(alias="dateFrom")
    flag: int = Field(0, alias="flag")

    async def emit(self, wb_api: WbAPI) -> list[Sale]:
        wb_api.session.headers.set_token(wb_api._token)
        url = wb_api.session.build_url(self.__api__, self.__method__)
        excluded_fields = {"request_limit"}

        params = self.model_dump(by_alias=True, exclude_none=True, exclude=excluded_fields)
        raw: Any = await wb_api.session.get(url, params=params, limit=self.request_limit)

        adapter = TypeAdapter(list[Sale])

        # flag=1 returns all sales for the given date in one response — no cursor needed
        if self.flag == 1:
            return adapter.validate_python(raw or [])

        # flag=0: paginate via lastChangeDate until empty response
        result: list[Sale] = []
        while raw:
            result.extend(adapter.validate_python(raw))
            next_date_from = raw[-1]["lastChangeDate"]
            params = {**params, "dateFrom": next_date_from}
            raw = await wb_api.session.get(url, params=params, limit=self.request_limit)

        return result
