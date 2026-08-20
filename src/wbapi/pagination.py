"""Pagination: one async iterator over every page an endpoint will return.

Wildberries uses several incompatible pagination schemes. The style is detected
from the first response, so callers write the same loop regardless::

    async for order in api.paginate("/api/v3/orders"):
        ...
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable
import logging
from typing import Any

from .types import wrap


__all__ = ("Paginator",)

log = logging.getLogger("wbapi.pagination")

Requester = Callable[..., Awaitable[Any]]

MAX_PAGES = 10_000

# Lists under these keys carry diagnostics, not the records we paginate over.
_NON_DATA_KEYS = frozenset({"errors", "error", "warnings", "additionalErrors"})
# Keys Wildberries commonly uses for the payload, checked before a blind scan.
_DATA_KEYS = ("data", "cards", "orders", "supplies", "stocks", "items", "result", "report")


def extract_items(raw: Any) -> list[Any]:
    """Find the list of records in a response body.

    Prefers known payload keys and skips diagnostic lists, so a body shaped
    like ``{"errors": [], "data": [...]}`` yields ``data`` rather than
    stopping on the empty ``errors`` list.
    """
    if isinstance(raw, list):
        return raw
    if not isinstance(raw, dict):
        return []

    for key in _DATA_KEYS:
        value = raw.get(key)
        if isinstance(value, list):
            return value

    for key, value in raw.items():
        if key not in _NON_DATA_KEYS and isinstance(value, list):
            return value

    for key, value in raw.items():
        if key not in _NON_DATA_KEYS and isinstance(value, dict):
            nested = extract_items(value)
            if nested:
                return nested

    return []


class Paginator:
    """Async iterator over every record across every page.

    Yields records one at a time, fetching each page only when the previous one
    is exhausted. Collect everything with a comprehension when you need a list::

        orders = [o async for o in api.paginate("/api/v3/orders")]
    """

    __slots__ = ("_request", "_page_size", "_params", "_body", "_pages")

    def __init__(
        self,
        request: Requester,
        *,
        page_size: int,
        params: dict[str, Any] | None = None,
        body: dict[str, Any] | None = None,
    ) -> None:
        self._request = request
        self._page_size = page_size
        self._params = dict(params or {})
        self._body = dict(body) if body is not None else None
        self._pages = 0

    def __repr__(self) -> str:
        mode = "POST" if self._body is not None else "GET"
        return f"Paginator({mode}, page_size={self._page_size})"

    async def __aiter__(self) -> AsyncIterator[Any]:
        async for page in self._raw_pages():
            for item in page:
                yield wrap(item)

    def _guard(self) -> None:
        self._pages += 1
        if self._pages > MAX_PAGES:
            raise RuntimeError(f"Pagination exceeded {MAX_PAGES} pages; aborting to avoid an infinite loop.")

    async def _raw_pages(self) -> AsyncIterator[list[Any]]:
        """Fetch the first page, pick a strategy, then follow it to the end."""
        if self._body is not None:
            body = {**self._body, "limit": self._page_size, "offset": 0}
            raw = await self._request(params=self._params or None, body=body)
        else:
            body = None
            self._params["limit"] = self._page_size
            raw = await self._request(params=self._params)

        self._guard()
        page = extract_items(raw)
        if page:
            yield page

        strategy = self._detect(raw, page)
        async for nxt in strategy(raw, page, body):
            self._guard()
            yield nxt

    def _detect(self, raw: Any, page: list[Any]) -> Callable[..., AsyncIterator[list[Any]]]:
        """Choose a pagination strategy from the shape of the first response.

        Order (first match wins): cursor → rrdId (POST) → next token →
        rrd_id (GET) → offset in body → offset in query.
        """
        last = page[-1] if page and isinstance(page[-1], dict) else None
        is_post = self._body is not None

        if is_post and isinstance(raw, dict):
            cursor = raw.get("cursor")
            if isinstance(cursor, dict) and "updatedAt" in cursor:
                return self._by_cursor

        if is_post and last is not None and "rrdId" in last:
            return self._by_rrdid_post

        if isinstance(raw, dict) and "next" in raw:
            return self._by_next_token

        if last is not None and "rrd_id" in last:
            return self._by_rrdid_query

        return self._by_offset_body if is_post else self._by_offset_query

    async def _by_next_token(
        self, raw: Any, page: list[Any], body: dict[str, Any] | None
    ) -> AsyncIterator[list[Any]]:
        """Token continuation: the response carries ``next``, echoed as ``?next=``.

        Used by Marketplace orders, FBW supplies, Q&A and reviews.
        """
        seen: set[Any] = set()
        while page:
            cursor = raw.get("next") if isinstance(raw, dict) else None
            if not cursor:
                return
            if cursor in seen:
                log.warning("Pagination cursor %r repeated; stopping.", cursor)
                return
            seen.add(cursor)

            raw = await self._request(params={**self._params, "limit": self._page_size, "next": cursor})
            page = extract_items(raw)
            if page:
                yield page

    async def _by_rrdid_query(
        self, raw: Any, page: list[Any], body: dict[str, Any] | None
    ) -> AsyncIterator[list[Any]]:
        """Finance reports (GET): the last row's ``rrd_id`` becomes ``?rrdid=``."""
        seen: set[Any] = set()
        while page:
            last = page[-1]
            rrd_id = last.get("rrd_id") if isinstance(last, dict) else None
            if not rrd_id or rrd_id in seen:
                return
            seen.add(rrd_id)

            raw = await self._request(params={**self._params, "rrdid": rrd_id})
            page = extract_items(raw)
            if page:
                yield page

    async def _by_rrdid_post(
        self, raw: Any, page: list[Any], body: dict[str, Any] | None
    ) -> AsyncIterator[list[Any]]:
        """Finance reports (POST): the last row's ``rrdId`` goes back in the body."""
        assert body is not None
        seen: set[Any] = set()
        while len(page) >= self._page_size:
            last = page[-1]
            rrd_id = last.get("rrdId") if isinstance(last, dict) else None
            if not rrd_id or rrd_id in seen:
                return
            seen.add(rrd_id)

            raw = await self._request(body={**body, "rrdId": rrd_id})
            page = extract_items(raw)
            if page:
                yield page

    async def _by_cursor(
        self, raw: Any, page: list[Any], body: dict[str, Any] | None
    ) -> AsyncIterator[list[Any]]:
        """Content v2 cards: merge the returned cursor into ``settings.cursor``."""
        assert body is not None
        while True:
            cursor = raw.get("cursor") if isinstance(raw, dict) else None
            if not isinstance(cursor, dict):
                return
            if cursor.get("total", 0) < self._page_size:
                return
            if "updatedAt" not in cursor or "nmID" not in cursor:
                log.warning("Cursor missing updatedAt/nmID; stopping pagination.")
                return

            settings = body.get("settings")
            raw = await self._request(
                body={
                    **body,
                    "settings": {
                        **(settings if isinstance(settings, dict) else {}),
                        "cursor": {
                            "limit": self._page_size,
                            "updatedAt": cursor["updatedAt"],
                            "nmID": cursor["nmID"],
                        },
                    },
                }
            )
            page = extract_items(raw)
            if page:
                yield page

    async def _by_offset_query(
        self, raw: Any, page: list[Any], body: dict[str, Any] | None
    ) -> AsyncIterator[list[Any]]:
        offset = self._page_size
        while len(page) >= self._page_size:
            raw = await self._request(params={**self._params, "limit": self._page_size, "offset": offset})
            page = extract_items(raw)
            if page:
                yield page
            offset += self._page_size

    async def _by_offset_body(
        self, raw: Any, page: list[Any], body: dict[str, Any] | None
    ) -> AsyncIterator[list[Any]]:
        assert body is not None
        offset = self._page_size
        while len(page) >= self._page_size:
            raw = await self._request(body={**body, "limit": self._page_size, "offset": offset})
            page = extract_items(raw)
            if page:
                yield page
            offset += self._page_size
