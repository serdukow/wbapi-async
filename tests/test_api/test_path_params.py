"""Tests for path parameter substitution in dispatch."""

from __future__ import annotations

import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestPathParams:
    async def test_single_param_substituted(self, api: MockedAPI) -> None:
        api.add_response({})
        await api.get("/api/v3/orders/{orderId}/meta", orderId=123)

        assert api.get_last_request().url.endswith("/api/v3/orders/123/meta")

    async def test_param_not_in_query_string(self, api: MockedAPI) -> None:
        api.add_response({})
        await api.get("/api/v3/orders/{orderId}/meta", orderId=123)

        params = api.get_last_request().params
        assert params is None or "orderId" not in params

    async def test_numeric_param_substituted(self, api: MockedAPI) -> None:
        api.add_response({})
        await api.get("/api/v3/orders/{orderId}/meta/gtin", orderId=456)

        assert api.get_last_request().url.endswith("/api/v3/orders/456/meta/gtin")

    async def test_string_param(self, api: MockedAPI) -> None:
        api.add_response({})
        await api.get("/api/v3/supplies/{supplyId}/barcode", supplyId="WB-GI-123456")

        assert api.get_last_request().url.endswith("/api/v3/supplies/WB-GI-123456/barcode")

    async def test_other_kwargs_remain_as_query_params(self, api: MockedAPI) -> None:
        api.add_response({})
        await api.get("/api/v3/orders/{orderId}/meta", orderId=123, someParam="value")

        req = api.get_last_request()
        assert req.params is not None and req.params["someParam"] == "value"
        assert "orderId" not in (req.params or {})

    async def test_no_params_unchanged(self, api: MockedAPI) -> None:
        api.add_response({"orders": [], "next": 0})
        await api.get("/api/v3/orders/new", limit=10, next=0)

        req = api.get_last_request()
        assert req.params == {"limit": 10, "next": 0}

    async def test_delete_with_path_param(self, api: MockedAPI) -> None:
        api.add_response({})
        await api.delete("/api/v3/passes/{passId}", passId=99)

        assert api.get_last_request().url.endswith("/api/v3/passes/99")
