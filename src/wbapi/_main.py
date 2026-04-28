from __future__ import annotations

from typing import Any

from ._core import BaseSession, MethodDispatcher
from .type import ApiResponse


class WbAPI:
    """
    Async client for the Wildberries Seller API.

    Source: https://dev.wildberries.ru/en/docs/openapi/api-information
    """

    def __init__(
        self,
        token: str,
        session: BaseSession | None = None,
        *,
        timeout: int = 60,
    ) -> None:
        self._token = token
        self.session = session or BaseSession(base="https://wildberries.ru", timeout=timeout)
        self._dispatcher = MethodDispatcher(self.session, token)

    async def get(self, path: str, *, paginate: bool = False, **kwargs: Any) -> ApiResponse:
        """
        Send a GET request.

        Example::

                await api.get("/api/v3/warehouses")
            orders = await api.get(
                "/api/v3/orders/new", limit=10, next=0
            )

                await api.get(
                    "/api/v1/supplier/orders",
                    dateFrom="2026-04-28",
                    flag=1,
                    paginate=True
            )
        """
        return await self._dispatcher.dispatch("GET", path, params=kwargs or None, paginate=paginate)

    async def post(
        self, path: str, *, body: Any = None, paginate: bool = False, **kwargs: Any
    ) -> ApiResponse:
        """
        Send a POST request.

        Example::

            await api.post(
                "/content/v2/get/cards/list",
                body={
                    "settings": {
                        "sort": {"ascending": True},
                        "filter": {"withPhoto": -1},
                        "cursor": {"limit": 100},
                    }
                },
                paginate=True,
            )
        """
        return await self._dispatcher.dispatch(
            "POST", path, json=body, params=kwargs or None, paginate=paginate
        )

    async def put(self, path: str, *, body: Any = None, **kwargs: Any) -> ApiResponse:
        """
        Send a PUT request.

        Example::

            await api.put(
                "/api/v3/stocks/1234567",
                body={"stocks": [{"sku": "WB007", "amount": 10}]},
            )
        """
        return await self._dispatcher.dispatch("PUT", path, json=body, params=kwargs or None)

    async def patch(self, path: str, *, body: Any = None, **kwargs: Any) -> ApiResponse:
        """
        Send a PATCH request.

        Example::
            await api.patch(
                "/api/v3/orders/{orderId}/cancel", orderId=13833711
            )
        """
        return await self._dispatcher.dispatch("PATCH", path, json=body, params=kwargs or None)

    async def delete(self, path: str, **kwargs: Any) -> ApiResponse:
        """
        Send a DELETE request.

        Example::

            await api.delete("/content/v2/tag/99")
        """
        return await self._dispatcher.dispatch("DELETE", path, params=kwargs or None)

    async def __aenter__(self) -> WbAPI:
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.session.close()
