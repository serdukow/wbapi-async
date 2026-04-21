"""Tests for per-endpoint page size overrides in _PAGE_SIZES."""

from __future__ import annotations

import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestPageSizes:
    async def test_default_endpoint_uses_1000(self, api: MockedAPI) -> None:
        api.add_response({"orders": [{"id": i} for i in range(10)], "next": 0})
        await api.get_all("/api/v3/orders")

        req = api.mocked_session.requests[0]
        assert req.params is not None and req.params["limit"] == 1000

    async def test_cards_list_uses_100(self, api: MockedAPI) -> None:
        api.add_response({"cards": [{"nmID": 1}]})
        await api.get_all("/content/v2/get/cards/list", body={"settings": {}})

        req = api.mocked_session.requests[0]
        assert req.json is not None and req.json["limit"] == 100

    async def test_documents_list_uses_50(self, api: MockedAPI) -> None:
        api.add_response({"documents": [{"id": 1}]})
        await api.get_all("/api/v1/documents/list")

        req = api.mocked_session.requests[0]
        assert req.params is not None and req.params["limit"] == 50

    async def test_cards_list_offset_increments_by_100(self, api: MockedAPI) -> None:
        page1 = [{"nmID": i} for i in range(100)]
        page2 = [{"nmID": i} for i in range(5)]
        api.add_response({"cards": page1})
        api.add_response({"cards": page2})

        await api.get_all("/content/v2/get/cards/list", body={"settings": {}})

        second = list(api.mocked_session.requests)[1]
        assert second.json is not None
        assert second.json["offset"] == 100
        assert second.json["limit"] == 100

    async def test_documents_list_offset_increments_by_50(self, api: MockedAPI) -> None:
        page1 = [{"id": i} for i in range(50)]
        page2 = [{"id": i} for i in range(3)]
        api.add_response({"documents": page1})
        api.add_response({"documents": page2})

        await api.get_all("/api/v1/documents/list")

        second = list(api.mocked_session.requests)[1]
        assert second.params is not None
        assert second.params["offset"] == 50
        assert second.params["limit"] == 50
