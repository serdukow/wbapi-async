from __future__ import annotations

from typing import Any

from ._core import BaseSession, MethodDispatcher


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

    async def get(self, path: str, *, paginate: bool = False, **kwargs: Any) -> Any:
        """
        Send a GET request. kwargs become query parameters.

        Pass ``paginate=True`` to fetch all pages automatically.
        Pagination type is detected from the first response:
        - ``next`` in response → token continuation (Marketplace, Supplies, Q&A)
        - ``rrd_id`` in last item → rrdid token (Finance reports)
        - fallback → offset (Analytics, Promotions, Reports)

        Example::

            warehouses = await api.get("/api/v3/warehouses")
            orders = await api.get(
                "/api/v3/orders/new", limit=10, next=0
            )

            all_orders = await api.get(
                "/api/v3/orders", paginate=True, dateFrom=1698045576
            )
            all_sales = await api.get(
                "/api/finance/v1/sales-reports/detailed",
                paginate=True,
                dateFrom="2024-01-01",
                dateTo="2024-01-31",
            )
        """
        return await self._dispatcher.dispatch("GET", path, params=kwargs or None, paginate=paginate)

    async def post(self, path: str, *, body: Any = None, paginate: bool = False, **kwargs: Any) -> Any:
        """
        Send a POST request. ``body`` is serialized as JSON. kwargs become query parameters.

        Pass ``paginate=True`` to fetch all pages automatically.
        Pagination type is detected from the first response:
        - ``cursor.updatedAt`` in response → cursor pagination (Content, cards list)
        - fallback → offset

        Example::

            await api.post(
                "/content/v2/get/cards/list",
                body={"settings": {"sort": {"ascending": False}}},
            )

            all_cards = await api.post(
                "/content/v2/get/cards/list",
                body={"settings": {"filter": {"withPhoto": -1}}},
                paginate=True,
            )
        """
        return await self._dispatcher.dispatch(
            "POST", path, json=body, params=kwargs or None, paginate=paginate
        )

    async def put(self, path: str, *, body: Any = None, **kwargs: Any) -> Any:
        """
        Send a PUT request. ``body`` is serialized as JSON. kwargs become query parameters.

        Example::

            await api.put(
                "/api/v3/stocks/1234567",
                body={"stocks": [{"sku": "WB007", "amount": 10}]},
            )
        """
        return await self._dispatcher.dispatch("PUT", path, json=body, params=kwargs or None)

    async def patch(self, path: str, *, body: Any = None, **kwargs: Any) -> Any:
        """
        Send a PATCH request. ``body`` is serialized as JSON. kwargs become query parameters.

        Example::

            await api.patch("/api/v3/orders/13833711/cancel")
            await api.patch("/content/v2/tag/99", body={"name": "sale"})
        """
        return await self._dispatcher.dispatch("PATCH", path, json=body, params=kwargs or None)

    async def delete(self, path: str, **kwargs: Any) -> Any:
        """
        Send a DELETE request. kwargs become query parameters.

        Example::

            await api.delete("/content/v2/tag/99")
            await api.delete("/api/v1/user", deletedUserID="abc-123")
        """
        return await self._dispatcher.dispatch("DELETE", path, params=kwargs or None)

    async def __aenter__(self) -> WbAPI:
        return self

    async def __aexit__(self, *_: Any) -> None:
        await self.session.close()
