from __future__ import annotations

from typing import TYPE_CHECKING, Any

from aiolimiter import AsyncLimiter

from ._registry import _BASES, _LIMITS, _PAGE_SIZES, _PUBLIC


if TYPE_CHECKING:
    from .client.session.base import BaseSession

_DEFAULT_LIMIT: tuple[int, int, int, int] = (60000, 60, 1000, 5)

_limiters: dict[tuple[int, int], AsyncLimiter] = {}


def _get_limiter(path: str) -> AsyncLimiter:
    period, limit, interval, burst = _LIMITS.get(path, _DEFAULT_LIMIT)
    key = (interval, burst)
    if key not in _limiters:
        _limiters[key] = AsyncLimiter(max_rate=burst, time_period=interval / 1000)
    return _limiters[key]


def resolve_url(path: str) -> str:
    """Resolve full URL for a spec path like /api/v3/supplies.

    If a full URL is passed, it is returned as-is provided its host is a known
    wildberries.ru domain or is listed in ``_PUBLIC``.
    """
    from urllib.parse import urlparse

    from .exceptions import WbAPIError

    if path.startswith("https://") or path.startswith("http://"):
        host = urlparse(path).netloc
        known_hosts = {urlparse(v).netloc for v in _BASES.values()} | _PUBLIC
        if host not in known_hosts:
            raise WbAPIError(detail=f"Unknown host {host!r}.")
        return path

    base = _BASES.get(path)
    if base:
        return base + path
    # Path may contain dynamic segments (e.g. /api/v3/supplies/WB-123/orders).
    # Walk up the path until we find a match.
    parts = path.rstrip("/").split("/")
    for i in range(len(parts) - 1, 0, -1):
        candidate = "/".join(parts[:i])
        if candidate in _BASES:
            return _BASES[candidate] + path
    raise WbAPIError(detail=f"Unknown path {path!r}. Check available paths at https://dev.wildberries.ru")


def _extract_list(raw: Any) -> list[Any] | None:
    if isinstance(raw, list):
        return raw
    if isinstance(raw, dict):
        for v in raw.values():
            if isinstance(v, list):
                return v
        for v in raw.values():
            if isinstance(v, dict):
                found = _extract_list(v)
                if found is not None:
                    return found
    return None


class MethodDispatcher:
    def __init__(self, session: BaseSession, token: str) -> None:
        self._session = session
        self._token = token

    async def dispatch(
        self,
        http_method: str,
        path: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any | None = None,
        no_auth: bool = False,
    ) -> Any:
        from urllib.parse import urlparse

        if not no_auth and path.startswith(("https://", "http://")):
            no_auth = urlparse(path).netloc in _PUBLIC

        if no_auth:
            self._session.headers.authorization = None
        else:
            self._session.headers.set_token(self._token)
        url = resolve_url(path)
        limiter = _get_limiter(path)
        return await self._session._request(http_method, url, params=params, json=json, limit=limiter)

    async def fetch_all(self, path: str, **kwargs: Any) -> list[Any]:
        """Fetch all pages. Accepts an optional ``paginator`` kwarg —
        a callable ``(response) -> (items, next_params | None)`` for custom pagination logic.

        Example::

            def my_paginator(raw):
                items = raw.get("result", [])
                cursor = raw.get("cursor") or None
                next_params = {"cursor": cursor} if cursor else None
                return items, next_params


            all_items = await api.get_all(
                "/api/v3/custom", paginator=my_paginator
            )
        """
        from .exceptions import PaginationNotSupported

        paginator = kwargs.pop("paginator", None)
        body = kwargs.pop("body", None)
        http_method = "POST" if body is not None else "GET"

        def _do_request(extra: dict[str, Any] | None = None, extra_body: dict[str, Any] | None = None) -> Any:
            if body is not None:
                json = {**body, **(extra or {}), **(extra_body or {})}
                return self.dispatch(http_method, path, params=kwargs or None, json=json)
            params = {**kwargs, **(extra or {})} or None
            return self.dispatch(http_method, path, params=params)

        if paginator is not None:
            result: list[Any] = []
            next_params: dict[str, Any] = {}
            while True:
                raw = await _do_request(next_params)
                items, next_params = paginator(raw)
                result.extend(items)
                if not next_params:
                    break
            return result

        from .utils.paginate import PAGINATION_STRATEGIES

        page_size = _PAGE_SIZES.get(path, 1000)
        first_extra: dict[str, Any] = {"limit": page_size}
        if body is not None:
            first_extra["offset"] = 0
        raw = await _do_request(first_extra)
        page = _extract_list(raw)

        if page is None:
            raise PaginationNotSupported(f"No list data found in response for {path!r}")

        result: list[Any] = list(page)

        for strategy in PAGINATION_STRATEGIES:
            if strategy.detect(raw, page, body, page_size):
                return await strategy.paginate(result, page, raw, _do_request, page_size)

        if not result:
            raise PaginationNotSupported(f"{path!r} returned empty first page — pagination not supported")
        return result
