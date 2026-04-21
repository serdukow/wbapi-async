from __future__ import annotations

from typing import Any

from ._method import MethodDispatcher
from .client.session.base import BaseSession
from .type import ApiResponse, _wrap


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

    async def get(self, path: str, **kwargs: Any) -> Any:
        """
        Send a GET request. kwargs become query parameters.

        Example::
            warehouses = await api.get("/api/v3/warehouses")
            orders = await api.get(
                "/api/v3/orders/new", limit=10, next=0
            )
            meta = await api.get(
                "/api/v3/orders/{orderId}/meta", orderId=123
            )
        """
        return _wrap(await self._dispatcher.dispatch("GET", path, params=kwargs or None))

    async def get_all(self, path: str, **kwargs: Any) -> list[ApiResponse]:
        """
        Fetch all pages from a paginated endpoint. Pass ``body=`` to use POST.

        Example::
            supplies = await api.get_all("/api/v3/supplies")
            cards = await api.get_all(
                "/content/v2/get/cards/list",
                body={"settings": {"sort": {"ascending": False}}},
            )
        """
        return [ApiResponse(item) for item in await self._dispatcher.fetch_all(path, **kwargs)]

    async def post(self, path: str, *, body: Any = None, **kwargs: Any) -> Any:
        """
        Send a POST request. ``body`` is serialized as JSON. kwargs become query parameters.

        Example::

            await api.post(
                "/content/v2/get/cards/list",
                body={
                    "settings": {
                        "sort": {"ascending": False},
                        "filter": {"textSearch": "12345"},
                    }
                },
            )
            await api.post(
                "/content/v2/tag/nomenclature/link",
                body={"nmID": 179891389, "tagsIDs": [123456]},
            )
            await api.post(
                "/adv/v0/rename",
                body={"advertId": 2233344, "name": "newname"},
            )
        """
        return _wrap(await self._dispatcher.dispatch("POST", path, json=body, params=kwargs or None))

    async def put(self, path: str, *, body: Any = None, **kwargs: Any) -> Any:
        """
        Send a PUT request. ``body`` is serialized as JSON. kwargs become query parameters.

        Example::

            await api.put(
                "/api/v3/stocks/1234567",
                body={"stocks": [{"sku": "WB007", "amount": 10}]},
            )
        """
        return _wrap(await self._dispatcher.dispatch("PUT", path, json=body, params=kwargs or None))

    async def patch(self, path: str, *, body: Any = None, **kwargs: Any) -> Any:
        """
        Send a PATCH request. ``body`` is serialized as JSON. kwargs become query parameters.

        Example::

            await api.patch("/api/v3/orders/13833711/cancel")
            await api.patch("/content/v2/tag/99", body={"name": "sale"})
        """
        return _wrap(await self._dispatcher.dispatch("PATCH", path, json=body, params=kwargs or None))

    async def delete(self, path: str, **kwargs: Any) -> Any:
        """
        Send a DELETE request. kwargs become query parameters.

        Example::

            await api.delete("/content/v2/tag/99")
            await api.delete("/api/v1/user", deletedUserID="abc-123")
        """
        return _wrap(await self._dispatcher.dispatch("DELETE", path, params=kwargs or None))

    async def __aenter__(self) -> WbAPI:
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.session.close()
