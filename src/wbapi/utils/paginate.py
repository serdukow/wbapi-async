from __future__ import annotations

from collections.abc import Callable
from typing import Any


_Requester = Callable[..., Any]


class PaginationStrategy:
    """Base class for pagination strategies used by fetch_all."""

    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int, path: str) -> bool:
        raise NotImplementedError

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int, body: Any
    ) -> list[Any]:
        raise NotImplementedError


class RrdIdBodyCursorStrategy(PaginationStrategy):
    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int, path: str) -> bool:
        return bool(body is not None and page and isinstance(page[-1], dict) and "rrdId" in page[-1])

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int, body: Any
    ) -> list[Any]:
        from .._method import _extract_list

        while len(page) >= page_size:
            rrd_id = page[-1]["rrdId"]
            page = _extract_list(await request(extra_body={"rrdId": rrd_id})) or []
            if not page:
                break
            result.extend(page)
        return result


class RrdIdCursorStrategy(PaginationStrategy):
    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int, path: str) -> bool:
        return bool(page and isinstance(page[-1], dict) and "rrd_id" in page[-1])

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int, body: Any
    ) -> list[Any]:
        from .._method import _extract_list

        while page:
            rrd_id = page[-1]["rrd_id"]
            page = _extract_list(await request({"rrdid": rrd_id})) or []
            result.extend(page)
        return result


class LastChangeDateStrategy(PaginationStrategy):
    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int, path: str) -> bool:
        return bool(page and isinstance(page[-1], dict) and "lastChangeDate" in page[-1])

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int, body: Any
    ) -> list[Any]:
        from .._method import _extract_list

        while page:
            date_from = page[-1]["lastChangeDate"]
            page = _extract_list(await request({"dateFrom": date_from})) or []
            result.extend(page)
        return result


class BodyCursorStrategy(PaginationStrategy):
    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int, path: str) -> bool:
        return body is not None and isinstance(raw, dict) and bool(raw.get("cursor"))

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int, body: Any
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
    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int, path: str) -> bool:
        return isinstance(raw, dict) and "next" in raw

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int, body: Any
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
    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int, path: str) -> bool:
        return len(page) >= page_size

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int, body: Any
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


class CardsListStrategy(PaginationStrategy):
    path = "/content/v2/get/cards/list"

    def detect(self, raw: Any, page: list[Any], body: Any, page_size: int, path: str) -> bool:
        if path != self.path:
            return False
        cursor = raw.get("cursor", {}) if isinstance(raw, dict) else {}
        return isinstance(cursor, dict) and "updatedAt" in cursor

    async def paginate(
        self, result: list[Any], page: list[Any], raw: Any, request: _Requester, page_size: int, body: Any
    ) -> list[Any]:
        cursor = raw.get("cursor", {}) if isinstance(raw, dict) else {}
        while cursor.get("total", 0) >= page_size:
            next_body = {
                **body,
                "settings": {
                    **body.get("settings", {}),
                    "cursor": {
                        "limit": page_size,
                        "updatedAt": cursor["updatedAt"],
                        "nmID": cursor["nmID"],
                    },
                },
            }
            raw = await request(full_body=next_body)
            page = raw.get("cards", []) if isinstance(raw, dict) else []
            result.extend(page)
            cursor = raw.get("cursor", {}) if isinstance(raw, dict) else {}
        return result


PAGINATION_STRATEGIES: list[PaginationStrategy] = [
    CardsListStrategy(),
    RrdIdBodyCursorStrategy(),
    RrdIdCursorStrategy(),
    LastChangeDateStrategy(),
    BodyCursorStrategy(),
    NextCursorStrategy(),
    OffsetStrategy(),
]
