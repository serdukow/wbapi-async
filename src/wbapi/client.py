"""The public client: :class:`WBApi`."""

from __future__ import annotations

from types import TracebackType
from typing import Any

import httpx

from .endpoints import page_size_for, resolve_url
from .exceptions import WBConfigurationError
from .pagination import Paginator
from .session import (
    DEFAULT_MAX_RETRIES,
    DEFAULT_MAX_RETRY_WAIT,
    DEFAULT_RETRY_BACKOFF,
    DEFAULT_TIMEOUT,
    Session,
    mask,
)
from .types import WBDict, WBList, wrap


__all__ = ("WBApi",)


class WBApi:
    """Async client for the Wildberries Seller API.

    Example::

        async with WBApi(token=os.environ["WB_TOKEN"]) as api:
            orders = await api.get(
                "/api/v3/orders/new", params={"limit": 10}
            )

            async for supply in api.paginate("/api/v3/supplies"):
                print(supply.id)

    Args:
        token: Seller API token, sent verbatim as the ``Authorization`` header.
        timeout: Seconds before a request is abandoned, or an ``httpx.Timeout``
            for per-phase control.
        max_retries: Retry attempts for 429, 5xx and network failures.
        retry_backoff: Base delay for exponential backoff, in seconds.
        max_retry_wait: Ceiling on any single backoff sleep, in seconds.
        user_agent: Overrides the default ``wbapi/<version>`` User-Agent.
        transport: Custom httpx transport, primarily for tests.

    Raises:
        WBConfigurationError: ``token`` is empty or not a string.

    Docs: https://dev.wildberries.ru/en/docs/openapi/api-information
    """

    __slots__ = ("_session",)

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
        if not isinstance(token, str) or not token.strip():
            raise WBConfigurationError("A non-empty API token is required.")

        self._session = Session(
            token.strip(),
            timeout=timeout,
            max_retries=max_retries,
            retry_backoff=retry_backoff,
            max_retry_wait=max_retry_wait,
            user_agent=user_agent,
            transport=transport,
        )

    def __repr__(self) -> str:
        return f"WBApi(token={mask(self._session._token)})"

    async def _call(
        self,
        method: str,
        path: str,
        params: dict[str, Any] | None,
        body: Any = None,
    ) -> WBDict | WBList | None:
        raw = await self._session.request(method, resolve_url(path), limit_key=path, params=params, json=body)
        wrapped: WBDict | WBList | None = wrap(raw)
        return wrapped

    async def get(self, path: str, *, params: dict[str, Any] | None = None) -> WBDict | WBList | None:
        """Send a GET request.

        Interpolate path ids yourself; the endpoint still keeps its own rate
        limit because the concrete path is matched back to its template.

        Example::

            await api.get(
                "/api/v1/supplier/orders",
                params={"dateFrom": "2026-04-28"},
            )
        """
        return await self._call("GET", path, params)

    async def post(
        self, path: str, *, body: Any = None, params: dict[str, Any] | None = None
    ) -> WBDict | WBList | None:
        """Send a POST request with ``body`` as the JSON payload.

        Example::

            await api.post(
                "/adv/v0/rename", body={"advertId": 123, "name": "new"}
            )
        """
        return await self._call("POST", path, params, body)

    async def put(
        self, path: str, *, body: Any = None, params: dict[str, Any] | None = None
    ) -> WBDict | WBList | None:
        """Send a PUT request.

        Example::

            await api.put(
                f"/api/v3/stocks/{warehouse_id}",
                body={"stocks": [{"sku": "WB007", "amount": 10}]},
            )
        """
        return await self._call("PUT", path, params, body)

    async def patch(
        self, path: str, *, body: Any = None, params: dict[str, Any] | None = None
    ) -> WBDict | WBList | None:
        """Send a PATCH request.

        Example::

            await api.patch(
                "/api/v3/orders/{orderId}/cancel",
                params={"orderId": 13833711},
            )
        """
        return await self._call("PATCH", path, params, body)

    async def delete(
        self, path: str, *, body: Any = None, params: dict[str, Any] | None = None
    ) -> WBDict | WBList | None:
        """Send a DELETE request.

        Example::

            await api.delete(f"/content/v2/tag/{tag_id}")
        """
        return await self._call("DELETE", path, params, body)

    def paginate(
        self,
        path: str,
        *,
        body: Any = None,
        params: dict[str, Any] | None = None,
        page_size: int | None = None,
    ) -> Paginator:
        """Iterate over every record the endpoint will return.

        The pagination scheme is detected from the first response. Passing
        ``body`` switches the endpoint to POST, which some paginated endpoints
        require.

        Example::

            async for order in api.paginate("/api/v3/orders"):
                await store(order)

            cards = [
                c
                async for c in api.paginate(
                    "/content/v2/get/cards/list",
                    body={"settings": {"filter": {"withPhoto": -1}}},
                )
            ]

        Args:
            path: Spec path or full URL.
            body: JSON body; its presence selects POST over GET.
            params: Query parameters and any ``{name}`` path values.
            page_size: Overrides the per-endpoint default page size.

        Returns:
            An async iterator over the endpoint's records.
        """
        method = "POST" if body is not None else "GET"
        url = resolve_url(path)

        async def request(
            params: dict[str, Any] | None = None,
            body: dict[str, Any] | None = None,
        ) -> Any:
            return await self._session.request(method, url, limit_key=path, params=params, json=body)

        return Paginator(
            request,
            page_size=page_size or page_size_for(path),
            params=params,
            body=body if body is not None else None,
        )

    @property
    def is_closed(self) -> bool:
        return self._session.is_closed

    async def close(self) -> None:
        await self._session.close()

    async def __aenter__(self) -> WBApi:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.close()
