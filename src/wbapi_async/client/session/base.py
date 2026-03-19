import asyncio
from typing import Any

from aiolimiter import AsyncLimiter
import httpx
from httpx import RequestError

from ...enums import Method
from ...exceptions import WbAPIError
from ...types import Request, RequestLimit, Response
from .headers import Headers


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
        """
        The WB API has request rate limits.
        To evenly distribute the load, the token bucket algorithm is used.
        Limits for specific API methods are specified in the documentation.

        Source: https://dev.wildberries.ru/en/docs/openapi/api-information#tag/Introduction/Rate-Limits
        :param limit:
        :return:
        """
        # interval is in milliseconds.
        # burst is the token bucket capacity (max simultaneous requests).
        key = (limit.burst, limit.interval)
        if key not in _limiters:
            _limiters[key] = AsyncLimiter(max_rate=limit.burst, time_period=limit.interval / 1000)
        return _limiters[key]

    async def make_request(
        self,
        request: Request,
        limit: RequestLimit | None = None,
    ) -> Response:
        if limit is not None:
            await self._get_limiter(limit).acquire()

        try:
            response = await self._client.request(
                method=request.method.upper(),
                url=request.url,
                params=request.params,
                json=request.json_data,
                content=request.data,
                headers=self.headers.model_dump(),
            )
        except RequestError:
            raise

        if response.status_code == 429:
            retry_after = int(response.headers.get("X-Ratelimit-Retry", 1))
            await asyncio.sleep(retry_after)
            return await self.make_request(request, limit=limit)

        if response.status_code >= 400:
            raise WbAPIError(
                http_status=response.status_code,
                **response.json(),
            ) from None

        data = response.json() if response.content else None
        return Response(status=response.status_code, ok=True, data=data)

    async def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        limit: RequestLimit | None = None,
    ) -> Response:
        req = Request(method=Method.GET, url=url, params=params)
        return await self.make_request(req, limit=limit)

    async def post(
        self,
        url: str,
        *,
        json: Any | None = None,
        data: str | bytes | None = None,
        limit: RequestLimit | None = None,
    ) -> Response:
        req = Request(method=Method.POST, url=url, json_data=json, data=data)
        return await self.make_request(req, limit=limit)

    async def put(
        self,
        url: str,
        *,
        json: Any | None = None,
        data: str | bytes | None = None,
        limit: RequestLimit | None = None,
    ) -> Response:
        req = Request(method=Method.PUT, url=url, json_data=json, data=data)
        return await self.make_request(req, limit=limit)

    async def delete(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        limit: RequestLimit | None = None,
    ) -> Response:
        req = Request(method=Method.DELETE, url=url, params=params)
        return await self.make_request(req, limit=limit)
