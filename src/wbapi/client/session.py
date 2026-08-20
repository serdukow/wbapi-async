from __future__ import annotations

import asyncio
import logging
import random
from typing import Any
from weakref import WeakKeyDictionary

from aiolimiter import AsyncLimiter
import httpx

from .endpoints import PUBLIC_HOSTS, rate_limit_for
from .exceptions import (
    WBConnectionError,
    WBRateLimitError,
    WBTimeoutError,
    error_for_status,
)


__all__ = ("Session",)

log = logging.getLogger("wbapi")

DEFAULT_TIMEOUT = 60.0
DEFAULT_MAX_RETRIES = 3
DEFAULT_RETRY_BACKOFF = 0.5
DEFAULT_MAX_RETRY_WAIT = 60.0

_RETRY_STATUSES = frozenset({429, 500, 502, 503, 504})
_RETRY_AFTER_HEADERS = ("X-Ratelimit-Retry", "Retry-After")
_ERROR_PREVIEW = 200

# Limiters are shared per event loop: Wildberries throttles per account, so
# concurrent clients must contend for one budget — but an AsyncLimiter is bound
# to the loop that created it. Keying weakly on the loop lets both the limiters
# and their entry disappear once that loop is collected.
_limiters: WeakKeyDictionary[asyncio.AbstractEventLoop, dict[tuple[int, int], AsyncLimiter]] = (
    WeakKeyDictionary()
)


def mask(token: str) -> str:
    if not token:
        return "<empty>"
    return f"…{token[-4:]}" if len(token) > 4 else "…"


def _limiter_for(path: str) -> AsyncLimiter:
    """Return the limiter governing ``path`` on the running event loop."""
    loop = asyncio.get_running_loop()
    per_loop = _limiters.get(loop)
    if per_loop is None:
        per_loop = {}
        _limiters[loop] = per_loop

    rate = rate_limit_for(path)
    limiter = per_loop.get(rate)
    if limiter is None:
        interval_ms, burst = rate
        limiter = AsyncLimiter(max_rate=burst, time_period=interval_ms / 1000)
        per_loop[rate] = limiter
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


class Session:
    """Owns the httpx client and applies the retry and rate-limit policy.

    The token is installed once as a client-level header rather than being
    swapped per request, so concurrent calls cannot race over credentials.
    """

    __slots__ = (
        "_token",
        "_client",
        "max_retries",
        "retry_backoff",
        "max_retry_wait",
        "user_agent",
    )

    def __init__(
        self,
        token: str,
        *,
        timeout: float | httpx.Timeout = DEFAULT_TIMEOUT,
        max_retries: int = DEFAULT_MAX_RETRIES,
        retry_backoff: float = DEFAULT_RETRY_BACKOFF,
        max_retry_wait: float = DEFAULT_MAX_RETRY_WAIT,
        user_agent: str | None = None,
        transport: httpx.AsyncBaseTransport | None = None,
    ) -> None:
        from . import __version__

        self._token = token
        self.max_retries = max(0, max_retries)
        self.retry_backoff = retry_backoff
        self.max_retry_wait = max_retry_wait
        self.user_agent = user_agent or f"wbapi/{__version__}"

        self._client = httpx.AsyncClient(
            timeout=timeout,
            transport=transport,
            headers={
                "Accept": "application/json",
                "Content-Type": "application/json",
                "User-Agent": self.user_agent,
                "Authorization": token,
            },
            limits=httpx.Limits(max_connections=100, max_keepalive_connections=20),
        )

    def __repr__(self) -> str:
        return f"Session(token={mask(self._token)}, max_retries={self.max_retries})"

    @property
    def is_closed(self) -> bool:
        return self._client.is_closed

    async def close(self) -> None:
        await self._client.aclose()

    def _backoff(self, attempt: int, hint: float | None) -> float:
        """Exponential backoff with full jitter; a server hint takes priority."""
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
        params: dict[str, Any] | None = None,
        json: Any = None,
    ) -> Any:
        """Perform one logical request, retrying transient failures.

        Args:
            method: HTTP verb.
            url: Absolute URL to call.
            limit_key: Spec path used to look up the rate limit — the template
                form (``/api/v3/orders/{orderId}``), not the substituted one.
            params: Query parameters.
            json: JSON request body.

        Returns:
            The decoded JSON body, or ``None`` for an empty response.

        Raises:
            WBTimeoutError: Request timed out and retries were exhausted.
            WBConnectionError: Connection failed and retries were exhausted.
            WBAPIError: Server returned 4xx/5xx; the subclass reflects the status.
        """
        limiter = _limiter_for(limit_key)
        headers = {"Authorization": ""} if httpx.URL(url).host in PUBLIC_HOSTS else None
        last_error: Exception | None = None

        for attempt in range(self.max_retries + 1):
            async with limiter:
                try:
                    response = await self._client.request(
                        method, url, params=params, json=json, headers=headers
                    )
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
        """Decode a final response, or raise the matching exception."""
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
