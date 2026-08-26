from __future__ import annotations

import asyncio
import logging
import random
from typing import Any
from weakref import WeakKeyDictionary

from aiolimiter import AsyncLimiter
import httpx

from ..exceptions import (
    WBConnectionError,
    WBRateLimitError,
    WBTimeoutError,
    error_for_status,
)
from ..utils.token import mask_token


__all__ = ("Session",)

log = logging.getLogger("wbapi")

DEFAULT_TIMEOUT = 60.0
DEFAULT_MAX_RETRIES = 3
DEFAULT_RETRY_BACKOFF = 0.5
DEFAULT_MAX_RETRY_WAIT = 60.0

DEFAULT_RATE_LIMIT = (1000, 5)

_RETRY_STATUSES = frozenset({429, 500, 502, 503, 504})
_RETRY_AFTER_HEADERS = ("X-Ratelimit-Retry", "Retry-After")
_ERROR_PREVIEW = 200

# Limiters are shared per event loop: the quota is per account, but an
# AsyncLimiter belongs to the loop that created it. A weak key lets both
# the limiters and their entry go when that loop is collected.
_limiters: WeakKeyDictionary[asyncio.AbstractEventLoop, dict[tuple[str, tuple[int, int]], AsyncLimiter]] = (
    WeakKeyDictionary()
)


def _limiter_for(path: str, rate: tuple[int, int] | None = None) -> AsyncLimiter:
    loop = asyncio.get_running_loop()
    per_loop = _limiters.get(loop)
    if per_loop is None:
        per_loop = {}
        _limiters[loop] = per_loop

    rate = rate or DEFAULT_RATE_LIMIT
    key = (path, rate)
    limiter = per_loop.get(key)
    if limiter is None:
        interval_ms, burst = rate
        limiter = AsyncLimiter(max_rate=burst, time_period=interval_ms / 1000)
        per_loop[key] = limiter
    return limiter


def _retry_after(response: httpx.Response, cap: float) -> float | None:
    for header in _RETRY_AFTER_HEADERS:
        raw = response.headers.get(header)
        if raw is None:
            continue
        try:
            seconds = float(raw)
        except (TypeError, ValueError):
            continue
        if seconds >= 0:
            return min(seconds, cap)
    return None


_BINARY_TYPES = ("application/zip", "application/pdf", "image/", "application/octet-stream")


class Session:
    __slots__ = (
        "_token",
        "_client",
        "max_retries",
        "retry_backoff",
        "max_retry_wait",
    )

    def __init__(
        self,
        token: str,
        *,
        timeout: float | httpx.Timeout = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        retry_backoff: float = DEFAULT_RETRY_BACKOFF,
        max_retry_wait: float = DEFAULT_MAX_RETRY_WAIT,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        from .. import __version__

        self._token = token
        self.max_retries = max(0, max_retries)
        self.retry_backoff = retry_backoff
        self.max_retry_wait = max_retry_wait

        self._client = httpx.AsyncClient(
            timeout=timeout,
            transport=transport,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": f"wbapi/{__version__}",
                "Authorization": token,
            },
            limits=httpx.Limits(max_connections=100, max_keepalive_connections=20),
        )

    def __repr__(self) -> str:
        return f"Session(token={mask_token(self._token)}, max_retries={self.max_retries})"

    @property
    def masked_token(self) -> str:
        return mask_token(self._token)

    async def close(self) -> None:
        await self._client.aclose()

    def _backoff(self, attempt: int, hint: float | None) -> float:
        if hint is not None:
            return hint
        window = min(self.retry_backoff * (2**attempt), self.max_retry_wait)
        return random.uniform(0, window)

    async def request(
        self,
        method: str,
        url: str,
        *,
        limit_key: str,
        rate_limit: tuple[int, int] | None = None,
        params: dict[str, Any] | None = None,
        json: Any = None,
    ) -> Any:
        limiter = _limiter_for(limit_key, rate_limit)

        last_error: Exception | None = None

        for attempt in range(self.max_retries + 1):
            async with limiter:
                try:
                    response = await self._client.request(method, url, params=params, json=json)
                except httpx.TimeoutException as exc:
                    last_error = WBTimeoutError(f"{method} {url} timed out: {exc}")
                except httpx.TransportError as exc:
                    last_error = WBConnectionError(f"{method} {url} failed: {exc}")
                else:
                    if response.status_code not in _RETRY_STATUSES or attempt == self.max_retries:
                        return self._handle(response, method, url)

                    delay = self._backoff(attempt, _retry_after(response, self.max_retry_wait))
                    log.warning(
                        "%s %s -> %d, retrying in %.2fs (%d/%d)",
                        method,
                        url,
                        response.status_code,
                        delay,
                        attempt + 1,
                        self.max_retries,
                    )
                    await asyncio.sleep(delay)
                    continue

            if attempt == self.max_retries:
                break

            delay = self._backoff(attempt, None)
            log.warning(
                "%s %s failed (%s), retrying in %.2fs (%d/%d)",
                method,
                url,
                type(last_error).__name__,
                delay,
                attempt + 1,
                self.max_retries,
            )
            await asyncio.sleep(delay)

        assert last_error is not None
        raise last_error

    def _handle(self, response: httpx.Response, method: str, url: str) -> Any:
        request_id = response.headers.get("X-Request-Id")

        if response.status_code >= 400:
            try:
                payload: Any = response.json() if response.content else None
            except ValueError:
                payload = response.text[:_ERROR_PREVIEW].strip() or None

            error_cls = error_for_status(response.status_code)
            kwargs: dict[str, Any] = {
                "status_code": response.status_code,
                "payload": payload,
                "request_id": request_id,
                "method": method,
                "path": url,
            }
            if error_cls is WBRateLimitError:
                kwargs["retry_after"] = _retry_after(response, self.max_retry_wait)
            raise error_cls(**kwargs)

        if not response.content:
            return None

        if response.headers.get("Content-Type", "").startswith(_BINARY_TYPES):
            return response.content

        try:
            return response.json()
        except ValueError as exc:
            raise error_for_status(response.status_code)(
                f"Failed to decode JSON response: {response.text[:_ERROR_PREVIEW]!r}",
                status_code=response.status_code,
                request_id=request_id,
                method=method,
                path=url,
            ) from exc
