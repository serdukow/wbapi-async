from __future__ import annotations

from collections.abc import Callable
from typing import Any


_Requester = Callable[..., Any]


class PaginationStrategy:
    """Base class for pagination strategies used by fetch_all."""

    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int) -> bool:
        raise NotImplementedError

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int
    ) -> list[Any]:
        raise NotImplementedError


class RrdIdCursorStrategy(PaginationStrategy):
    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int) -> bool:
        return bool(page and isinstance(page[-1], dict) and "rrd_id" in page[-1])

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int
    ) -> list[Any]:
        from .._method import _extract_list

        while page:
            rrd_id = page[-1]["rrd_id"]
            page = _extract_list(await request({"rrdid": rrd_id})) or []
            result.extend(page)
        return result


class LastChangeDateStrategy(PaginationStrategy):
    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int) -> bool:
        return bool(page and isinstance(page[-1], dict) and "lastChangeDate" in page[-1])

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int
    ) -> list[Any]:
        from .._method import _extract_list

        while page:
            date_from = page[-1]["lastChangeDate"]
            page = _extract_list(await request({"dateFrom": date_from})) or []
            result.extend(page)
        return result


class BodyCursorStrategy(PaginationStrategy):
    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int) -> bool:
        return body is not None and isinstance(raw, dict) and bool(raw.get("cursor"))

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int
    ) -> list[Any]:
        from .._method import _extract_list

        cursor_val = raw.get("cursor")
        while cursor_val:
            raw = await request(extra_body={"cursor": cursor_val})
            page = _extract_list(raw)
            if not page:
                break
            result.extend(page)
            cursor_val = raw.get("cursor") if isinstance(raw, dict) else None
        return result


class NextCursorStrategy(PaginationStrategy):
    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int) -> bool:
        return isinstance(raw, dict) and "next" in raw

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int
    ) -> list[Any]:
        from .._method import _extract_list

        cursor = raw["next"]
        while cursor:
            raw = await request({"limit": page_size, "next": cursor})
            page = _extract_list(raw)
            if not page:
                break
            result.extend(page)
            cursor = raw.get("next") if isinstance(raw, dict) else None
        return result


class OffsetStrategy(PaginationStrategy):
    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int) -> bool:
        return len(page) >= page_size

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int
    ) -> list[Any]:
        from .._method import _extract_list

        offset = page_size
        while True:
            raw = await request({"limit": page_size, "offset": offset})
            page = _extract_list(raw)
            if not page:
                break
            result.extend(page)
            if len(page) < page_size:
                break
            offset += page_size
        return result


PAGINATION_STRATEGIES: list[PaginationStrategy] = [
    RrdIdCursorStrategy(),
    LastChangeDateStrategy(),
    BodyCursorStrategy(),
    NextCursorStrategy(),
    OffsetStrategy(),
]
