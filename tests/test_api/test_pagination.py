"""Tests for paginate=True auto-pagination across all WB API pagination types."""

from __future__ import annotations

import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestNextTokenPagination:
    """Marketplace orders, Supplies FBW, Q&A — ``next`` token in response root."""

    async def test_single_page_next_zero_stops(self, api: MockedAPI) -> None:
        # Arrange
        api.add_response({"orders": [{"id": 1}], "next": 0})

        # Act
        result = await api.get("/api/v3/orders", paginate=True, dateFrom=1698045576)

        # Assert
        assert len(result) == 1
        assert result[0].id == 1

    async def test_two_pages_next_forwarded(self, api: MockedAPI) -> None:
        # Arrange
        page1 = [{"id": i} for i in range(1000)]
        page2 = [{"id": i} for i in range(50)]
        api.add_response({"orders": page1, "next": 99999})
        api.add_response({"orders": page2, "next": 0})

        # Act
        result = await api.get("/api/v3/orders", paginate=True, dateFrom=1698045576)

        # Assert
        assert len(result) == 1050
        req2 = api.mocked_session.requests[1]
        assert req2.params["next"] == 99999

    async def test_empty_first_page_stops(self, api: MockedAPI) -> None:
        # Arrange
        api.add_response({"orders": [], "next": 0})

        # Act
        result = await api.get("/api/v3/orders", paginate=True, dateFrom=1698045576)

        # Assert
        assert result == []

    async def test_three_pages_accumulates_all(self, api: MockedAPI) -> None:
        # Arrange
        api.add_response({"orders": [{"id": i} for i in range(1000)], "next": 111})
        api.add_response({"orders": [{"id": i} for i in range(1000)], "next": 222})
        api.add_response({"orders": [{"id": i} for i in range(7)], "next": 0})

        # Act
        result = await api.get("/api/v3/orders", paginate=True, dateFrom=1698045576)

        # Assert
        assert len(result) == 2007
        assert len(api.mocked_session.requests) == 3


@pytest.mark.unit
class TestRrdidTokenPagination:
    """Finance reports — ``rrd_id`` in last item, sent as ``?rrdid=``."""

    async def test_two_pages_rrdid_forwarded(self, api: MockedAPI) -> None:
        # Arrange
        page1 = [{"rrd_id": i + 1, "amount": i * 10} for i in range(1000)]
        page2 = [{"rrd_id": 1001, "amount": 999}]
        api.add_response(page1)
        api.add_response(page2)
        api.add_response([])

        # Act
        result = await api.get(
            "/api/v5/supplier/reportDetailByPeriod",
            paginate=True,
            dateFrom="2024-01-01",
            dateTo="2024-01-31",
        )

        # Assert
        assert len(result) == 1001
        req2 = api.mocked_session.requests[1]
        assert req2.params["rrdid"] == 1000

    async def test_empty_page_stops(self, api: MockedAPI) -> None:
        # Arrange
        page1 = [{"rrd_id": 5, "amount": 100}]
        api.add_response(page1)
        api.add_response([])

        # Act
        result = await api.get(
            "/api/v5/supplier/reportDetailByPeriod",
            paginate=True,
            dateFrom="2024-01-01",
            dateTo="2024-01-31",
        )

        # Assert
        assert len(result) == 1
        assert len(api.mocked_session.requests) == 2


@pytest.mark.unit
class TestOffsetPagination:
    """Analytics, Promotions, Reports — ``offset`` incremented by ``limit``."""

    async def test_partial_first_page_stops_immediately(self, api: MockedAPI) -> None:
        # Arrange
        api.add_response({"items": [{"id": 1}, {"id": 2}]})

        # Act
        result = await api.get("/api/v3/supplies", paginate=True)

        # Assert
        assert len(result) == 2
        assert len(api.mocked_session.requests) == 1

    async def test_full_page_then_partial_stops(self, api: MockedAPI) -> None:
        # Arrange
        api.add_response({"items": [{"id": i} for i in range(1000)]})
        api.add_response({"items": [{"id": i} for i in range(3)]})

        # Act
        result = await api.get("/api/v3/supplies", paginate=True)

        # Assert
        assert len(result) == 1003
        assert api.mocked_session.requests[1].params["offset"] == 1000

    async def test_three_pages_offset_increments(self, api: MockedAPI) -> None:
        # Arrange
        full_page = [{"id": i} for i in range(1000)]
        api.add_response({"items": full_page})
        api.add_response({"items": full_page})
        api.add_response({"items": [{"id": 0}]})

        # Act
        result = await api.get("/api/v3/supplies", paginate=True)

        # Assert
        assert len(result) == 2001
        assert api.mocked_session.requests[2].params["offset"] == 2000

    async def test_list_response_directly(self, api: MockedAPI) -> None:
        # Arrange
        api.add_response([{"id": i} for i in range(5)])

        # Act
        result = await api.get("/api/v3/supplies", paginate=True)

        # Assert
        assert len(result) == 5

    async def test_empty_first_page_returns_empty(self, api: MockedAPI) -> None:
        # Arrange
        api.add_response({"items": []})

        # Act
        result = await api.get("/api/v3/supplies", paginate=True)

        # Assert
        assert result == []


@pytest.mark.unit
class TestCursorPagination:
    """Content cards list — ``cursor`` object in POST body response."""

    async def test_single_page_total_less_than_limit_stops(self, api: MockedAPI) -> None:
        # Arrange
        cards = [{"nmID": i} for i in range(50)]
        api.add_response({"cards": cards, "cursor": {"updatedAt": "2026-04-03T10:00:00Z", "nmID": 100, "total": 50}})

        # Act
        result = await api.post(
            "/content/v2/get/cards/list",
            body={"settings": {"filter": {"withPhoto": -1}}},
            paginate=True,
        )

        # Assert
        assert len(result) == 50
        assert len(api.mocked_session.requests) == 1

    async def test_two_pages_cursor_merged_into_body(self, api: MockedAPI) -> None:
        # Arrange
        page1 = [{"nmID": i} for i in range(100)]
        page2 = [{"nmID": i} for i in range(40)]
        api.add_response({"cards": page1, "cursor": {"updatedAt": "2026-04-03T10:00:00Z", "nmID": 370870300, "total": 100}})
        api.add_response({"cards": page2, "cursor": {"updatedAt": "2026-04-04T10:00:00Z", "nmID": 370870340, "total": 40}})

        # Act
        result = await api.post(
            "/content/v2/get/cards/list",
            body={"settings": {"filter": {"withPhoto": -1}}},
            paginate=True,
        )

        # Assert
        assert len(result) == 140
        req2 = api.mocked_session.requests[1]
        assert req2.json["settings"]["cursor"]["updatedAt"] == "2026-04-03T10:00:00Z"
        assert req2.json["settings"]["cursor"]["nmID"] == 370870300
        assert req2.json["settings"]["cursor"]["limit"] == 100

    async def test_original_settings_preserved_in_next_request(self, api: MockedAPI) -> None:
        # Arrange
        page1 = [{"nmID": i} for i in range(100)]
        page2 = [{"nmID": i} for i in range(5)]
        api.add_response({"cards": page1, "cursor": {"updatedAt": "2026-04-03T10:00:00Z", "nmID": 999, "total": 100}})
        api.add_response({"cards": page2, "cursor": {"updatedAt": "2026-04-04T10:00:00Z", "nmID": 1000, "total": 5}})

        # Act
        await api.post(
            "/content/v2/get/cards/list",
            body={"settings": {"filter": {"withPhoto": -1}, "sort": {"ascending": False}}},
            paginate=True,
        )

        # Assert — filter and sort preserved alongside cursor
        req2 = api.mocked_session.requests[1]
        assert req2.json["settings"]["filter"] == {"withPhoto": -1}
        assert req2.json["settings"]["sort"] == {"ascending": False}


@pytest.mark.unit
class TestPaginateFirstRequest:
    """Verify limit is always sent on the first request."""

    async def test_get_sends_limit_on_first_request(self, api: MockedAPI) -> None:
        api.add_response({"orders": [{"id": 1}], "next": 0})
        await api.get("/api/v3/orders", paginate=True)
        assert api.mocked_session.requests[0].params["limit"] == 1000

    async def test_post_sends_limit_on_first_request(self, api: MockedAPI) -> None:
        api.add_response({"cards": [{"nmID": 1}], "cursor": {"updatedAt": "x", "nmID": 1, "total": 1}})
        await api.post("/content/v2/get/cards/list", body={"settings": {}}, paginate=True)
        assert api.mocked_session.requests[0].params["limit"] == 100

    async def test_deeply_nested_list_extracted(self, api: MockedAPI) -> None:
        api.add_response({"data": {"products": [{"id": i} for i in range(3)], "currency": "RUB"}, "next": 0})
        result = await api.get("/api/v3/supplies", paginate=True)
        assert len(result) == 3
