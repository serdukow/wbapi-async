import asyncio
import logging
from typing import Any

from aiolimiter import AsyncLimiter
import httpx
from httpx import RequestError

from ...exceptions import WbAPIError
from ...types import RequestLimit
from .headers import Headers


logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)


# Shared limiters keyed by (burst, interval) — one token bucket per unique
# rate-limit config, shared across all instances and method calls.
_limiters: dict[tuple[int, int], AsyncLimiter] = {}


class BaseSession:
    base_url: str
    timeout: int
    headers: Headers

    def __init__(
        self,
        base: str,
        timeout: int = 30,
    ) -> None:
        self.base_url = base.rstrip("/")
        self.timeout = timeout
        self.headers = Headers()
        self._client = httpx.AsyncClient(timeout=self.timeout)

    def build_url(self, api: str, method: str) -> str:
        base = self.base_url.removeprefix("https://").removeprefix("http://")
        return f"https://{api}.{base}/{method}"

    async def close(self) -> None:
        await self._client.aclose()

    @staticmethod
    def _get_limiter(limit: RequestLimit) -> AsyncLimiter:
        key = (limit.burst, limit.interval)
        if key not in _limiters:
            _limiters[key] = AsyncLimiter(max_rate=limit.burst, time_period=limit.interval / 1000)
        return _limiters[key]

    async def _request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any | None = None,
        limit: RequestLimit | None = None,
    ) -> Any:
        if limit is not None:
            await self._get_limiter(limit).acquire()

        try:
            response = await self._client.request(
                method=method,
                url=url,
                params=params,
                json=json,
                headers=self.headers.model_dump(),
            )
        except RequestError:
            raise

        if response.status_code == 429:
            retry_after = int(response.headers.get("X-Ratelimit-Retry", 1))
            await asyncio.sleep(retry_after)
            return await self._request(method, url, params=params, json=json, limit=limit)

        if response.status_code >= 400:
            body: dict[str, object]
            if response.content:
                try:
                    body = response.json()
                except Exception:
                    body = {"detail": response.text.strip() or None}
            else:
                body = {"detail": None}
            raise WbAPIError(http_status=response.status_code, **body)

        if not response.content:
            return None
        try:
            return response.json()
        except Exception:
            return None

    async def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        limit: RequestLimit | None = None,
    ) -> Any:
        return await self._request("GET", url, params=params, limit=limit)

    async def post(
        self,
        url: str,
        *,
        json: Any | None = None,
        limit: RequestLimit | None = None,
    ) -> Any:
        return await self._request("POST", url, json=json, limit=limit)

    async def put(
        self,
        url: str,
        *,
        json: Any | None = None,
        limit: RequestLimit | None = None,
    ) -> Any:
        return await self._request("PUT", url, json=json, limit=limit)

    async def patch(
        self,
        url: str,
        *,
        json: Any | None = None,
        limit: RequestLimit | None = None,
    ) -> Any:
        return await self._request("PATCH", url, json=json, limit=limit)

    async def delete(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        limit: RequestLimit | None = None,
    ) -> Any:
        return await self._request("DELETE", url, params=params, limit=limit)
