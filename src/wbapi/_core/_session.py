import asyncio
from datetime import datetime, timedelta
import logging
from typing import Any

from aiolimiter import AsyncLimiter
import httpx
from httpx import RequestError

from ..exceptions import WBAPIError


log = logging.getLogger("wbapi.session")
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("httpcore").setLevel(logging.WARNING)


class Headers:
    def __init__(self) -> None:
        self.accept = "application/json;charset=utf-8"
        self.content_type = "application/json"
        self.authorization: str | None = None
        self.user_agent = (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/124.0.0.0 Safari/537.36"
        )

    def set_token(self, token: str) -> None:
        self.authorization = f"Bearer {token}"

    def as_dict(self) -> dict[str, str]:
        headers: dict[str, str] = {
            "Accept": self.accept,
            "Content-Type": self.content_type,
            "User-Agent": self.user_agent,
        }
        if self.authorization is not None:
            headers["Authorization"] = self.authorization
        return headers


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

    async def close(self) -> None:
        await self._client.aclose()

    async def _request(
        self,
        method: str,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        json: Any | None = None,
        limit: AsyncLimiter | None = None,
    ) -> Any:
        if limit is not None:
            await limit.acquire()

        try:
            response = await self._client.request(
                method=method,
                url=url,
                params=params,
                json=json,
                headers=self.headers.as_dict(),
            )
        except RequestError:
            raise

        if response.status_code == 429:
            retry_after = int(response.headers.get("X-Ratelimit-Retry", "1"))
            if retry_after > 60:
                retry_at = datetime.now() + timedelta(seconds=retry_after)
                log.warning(
                    "Rate limit exceeded. Retrying in %s seconds (at %s)",
                    retry_after,
                    retry_at,
                )
            await asyncio.sleep(retry_after)
            return await self._request(method, url, params=params, json=json, limit=limit)

        if response.status_code >= 400:
            try:
                detail = response.json() if response.content else {}
            except Exception:
                detail = {"detail": response.text.strip() or None}
            raise WBAPIError(http_status=response.status_code, **detail)

        if not response.content:
            return None

        try:
            return response.json()
        except Exception as e:
            raise WBAPIError(
                http_status=response.status_code,
                detail=f"Failed to decode JSON response: {response.text[:200]!r}",
            ) from e

    async def get(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        limit: AsyncLimiter | None = None,
    ) -> Any:
        return await self._request("GET", url, params=params, limit=limit)

    async def post(
        self,
        url: str,
        *,
        json: Any | None = None,
        limit: AsyncLimiter | None = None,
    ) -> Any:
        return await self._request("POST", url, json=json, limit=limit)

    async def put(
        self,
        url: str,
        *,
        json: Any | None = None,
        limit: AsyncLimiter | None = None,
    ) -> Any:
        return await self._request("PUT", url, json=json, limit=limit)

    async def patch(
        self,
        url: str,
        *,
        json: Any | None = None,
        limit: AsyncLimiter | None = None,
    ) -> Any:
        return await self._request("PATCH", url, json=json, limit=limit)

    async def delete(
        self,
        url: str,
        *,
        params: dict[str, Any] | None = None,
        limit: AsyncLimiter | None = None,
    ) -> Any:
        return await self._request("DELETE", url, params=params, limit=limit)
