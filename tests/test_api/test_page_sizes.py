"""Tests for per-endpoint page size overrides in _PAGE_SIZES."""

from __future__ import annotations

import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestPageSizes:
    async def test_default_endpoint_uses_1000(self, api: MockedAPI) -> None:
        # Arrange
        api.add_response({"orders": [{"id": i} for i in range(10)], "next": 0})

        # Act
        await api.get("/api/v3/orders", paginate=True)

        # Assert
        req = api.mocked_session.requests[0]
        assert req.params is not None and req.params["limit"] == 1000

    async def test_cards_list_body_preserved(self, api: MockedAPI) -> None:
        # Arrange
        api.add_response({
            "cards": [{"nmID": 1}],
            "cursor": {"updatedAt": "2026-01-01T00:00:00Z", "nmID": 1, "total": 1},
        })

        # Act
        await api.post("/content/v2/get/cards/list", body={"settings": {"cursor": {"limit": 100}}}, paginate=True)

        # Assert — body passed as-is, no limit injected into params
        req = api.mocked_session.requests[0]
        assert req.params is None
        assert req.json == {"settings": {"cursor": {"limit": 100}}}

    async def test_documents_list_uses_50(self, api: MockedAPI) -> None:
        # Arrange
        api.add_response({"documents": [{"id": 1}]})

        # Act
        await api.get("/api/v1/documents/list", paginate=True)

        # Assert
        req = api.mocked_session.requests[0]
        assert req.params is not None and req.params["limit"] == 50

    async def test_cards_list_cursor_uses_limit_100(self, api: MockedAPI) -> None:
        # Arrange — two pages, cursor pagination
        page1 = [{"nmID": i} for i in range(100)]
        page2 = [{"nmID": i} for i in range(5)]
        api.add_response({"cards": page1, "cursor": {"updatedAt": "2026-01-01T00:00:00Z", "nmID": 999, "total": 100}})
        api.add_response({"cards": page2, "cursor": {"updatedAt": "2026-01-02T00:00:00Z", "nmID": 1000, "total": 5}})

        # Act
        await api.post("/content/v2/get/cards/list", body={"settings": {}}, paginate=True)

        # Assert — second request cursor carries limit=100
        second = api.mocked_session.requests[1]
        assert second.json is not None
        assert second.json["settings"]["cursor"]["limit"] == 100

    async def test_documents_list_offset_increments_by_50(self, api: MockedAPI) -> None:
        # Arrange
        page1 = [{"id": i} for i in range(50)]
        page2 = [{"id": i} for i in range(3)]
        api.add_response({"documents": page1})
        api.add_response({"documents": page2})

        # Act
        await api.get("/api/v1/documents/list", paginate=True)

        # Assert
        second = api.mocked_session.requests[1]
        assert second.params is not None
        assert second.params["offset"] == 50
        assert second.params["limit"] == 50
