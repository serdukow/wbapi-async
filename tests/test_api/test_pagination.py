"""Tests for get_all() auto-pagination (cursor and offset detection)."""

from __future__ import annotations

import pytest

from tests.mocked_api import MockedAPI
from wbapi import PaginationNotSupported


@pytest.mark.unit
class TestCursorPagination:
    async def test_single_page_cursor_zero_stops(self, api: MockedAPI) -> None:
        api.add_response({"orders": [{"id": 1}], "next": 0})
        result = await api.get_all("/api/v3/orders")

        assert len(result) == 1
        assert result[0].id == 1

    async def test_two_pages_cursor_forwarded(self, api: MockedAPI) -> None:
        page1 = [{"id": i} for i in range(1000)]
        page2 = [{"id": i} for i in range(50)]
        api.add_response({"orders": page1, "next": 99999})
        api.add_response({"orders": page2, "next": 0})

        result = await api.get_all("/api/v3/orders")

        assert len(result) == 1050
        req = api.mocked_session.requests[1]
        assert req.params["next"] == 99999

    async def test_empty_first_page_cursor_returns_empty(self, api: MockedAPI) -> None:
        api.add_response({"orders": [], "next": 0})
        result = await api.get_all("/api/v3/orders")
        assert result == []


@pytest.mark.unit
class TestOffsetPagination:
    async def test_partial_first_page_stops(self, api: MockedAPI) -> None:
        api.add_response({"items": [{"id": 1}, {"id": 2}]})
        result = await api.get_all("/api/v3/supplies")

        assert len(result) == 2
        req = api.mocked_session.requests[-1]
        assert req.params["limit"] == 1000

    async def test_full_page_then_partial_stops(self, api: MockedAPI) -> None:
        page1 = [{"id": i} for i in range(1000)]
        page2 = [{"id": i} for i in range(3)]
        api.add_response({"items": page1})
        api.add_response({"items": page2})

        result = await api.get_all("/api/v3/supplies")

        assert len(result) == 1003
        assert len(api.mocked_session.requests) == 2
        assert api.mocked_session.requests[1].params["offset"] == 1000

    async def test_three_pages(self, api: MockedAPI) -> None:
        full_page = [{"id": i} for i in range(1000)]
        api.add_response({"items": full_page})
        api.add_response({"items": full_page})
        api.add_response({"items": [{"id": 0}]})

        result = await api.get_all("/api/v3/supplies")

        assert len(result) == 2001
        assert api.mocked_session.requests[2].params["offset"] == 2000

    async def test_list_response_directly(self, api: MockedAPI) -> None:
        api.add_response([{"id": i} for i in range(5)])
        result = await api.get_all("/api/v3/supplies")
        assert len(result) == 5


@pytest.mark.unit
class TestPostPagination:
    async def test_body_triggers_post(self, api: MockedAPI) -> None:
        api.add_response({"cards": [{"nmID": 1}]})
        await api.get_all("/content/v2/get/cards/list", body={"settings": {}})

        assert api.mocked_session.requests[0].method == "POST"

    async def test_body_sent_in_json(self, api: MockedAPI) -> None:
        api.add_response({"cards": [{"nmID": 1}]})
        await api.get_all("/content/v2/get/cards/list", body={"settings": {"ascending": False}})

        req = api.get_last_request()
        assert req.json == {"settings": {"ascending": False}, "limit": 100, "offset": 0}

    async def test_two_pages_post(self, api: MockedAPI) -> None:
        page1 = [{"nmID": i} for i in range(100)]
        page2 = [{"nmID": i} for i in range(5)]
        api.add_response({"cards": page1})
        api.add_response({"cards": page2})

        result = await api.get_all("/content/v2/get/cards/list", body={"settings": {}})

        assert len(result) == 105
        second = list(api.mocked_session.requests)[1]
        assert second.method == "POST"
        assert second.json is not None and second.json["offset"] == 100


@pytest.mark.unit
class TestPostBodyCursorPagination:
    async def test_cursor_in_body_response_continues(self, api: MockedAPI) -> None:
        api.add_response({"cards": [{"nmID": i} for i in range(3)], "cursor": "abc"})
        api.add_response({"cards": [{"nmID": 10}], "cursor": None})

        result = await api.get_all("/content/v2/get/cards/list", body={"settings": {}})

        assert len(result) == 4
        req2 = list(api.mocked_session.requests)[1]
        assert req2.json is not None and req2.json["cursor"] == "abc"

    async def test_cursor_none_stops(self, api: MockedAPI) -> None:
        api.add_response({"cards": [{"nmID": 1}], "cursor": None})

        result = await api.get_all("/content/v2/get/cards/list", body={"settings": {}})

        assert len(result) == 1
        assert len(api.mocked_session.requests) == 1


@pytest.mark.unit
class TestAutoDetectedCursors:
    async def test_rrd_id_cursor(self, api: MockedAPI) -> None:
        page1 = [{"id": i, "rrd_id": i + 1} for i in range(3)]
        page2 = [{"id": 10, "rrd_id": 10}]
        api.add_response({"items": page1})
        api.add_response({"items": page2})
        api.add_response({"items": []})

        result = await api.get_all("/api/v3/supplies")

        assert len(result) == 4
        req2 = list(api.mocked_session.requests)[1]
        assert req2.params is not None and req2.params["rrdid"] == 3

    async def test_last_change_date_cursor(self, api: MockedAPI) -> None:
        page1 = [{"id": i, "lastChangeDate": f"2024-01-0{i+1}"} for i in range(3)]
        page2 = [{"id": 10, "lastChangeDate": "2024-01-10"}]
        api.add_response({"items": page1})
        api.add_response({"items": page2})
        api.add_response({"items": []})

        result = await api.get_all("/api/v3/supplies")

        assert len(result) == 4
        req2 = list(api.mocked_session.requests)[1]
        assert req2.params is not None and req2.params["dateFrom"] == "2024-01-03"


@pytest.mark.unit
class TestCustomPaginator:
    async def test_auto_detects_deeply_nested_list(self, api: MockedAPI) -> None:
        # list is inside data.products — requires recursive _extract_list
        api.add_response({"data": {"products": [{"id": i} for i in range(3)], "currency": "RUB"}, "next": 0})
        result = await api.get_all("/api/v3/supplies")
        assert len(result) == 3
        assert result[0].id == 0

    async def test_paginator_cursor_from_last_item(self, api: MockedAPI) -> None:
        # e.g. /api/v1/supplier/reportDetailByPeriod — returns list directly,
        # next page starts from lastChangeDate of last item
        page1 = [{"id": i, "lastChangeDate": f"2024-01-0{i+1}"} for i in range(3)]
        page2 = [{"id": 10, "lastChangeDate": "2024-01-10"}]
        api.add_response(page1)
        api.add_response(page2)
        api.add_response([])  # empty page signals end

        def paginator(raw):
            items = raw if isinstance(raw, list) else []
            next_params = {"dateFrom": items[-1]["lastChangeDate"]} if items else None
            return items, next_params

        result = await api.get_all("/api/v3/supplies", paginator=paginator)
        assert len(result) == 4
        req2 = list(api.mocked_session.requests)[1]
        assert req2.params is not None and req2.params["dateFrom"] == "2024-01-03"

    async def test_custom_paginator_handles_nested(self, api: MockedAPI) -> None:
        api.add_response({"data": {"products": [{"id": 1}, {"id": 2}], "cursor": "abc"}})
        api.add_response({"data": {"products": [{"id": 3}], "cursor": None}})

        def paginator(raw):
            items = raw["data"]["products"]
            cursor = raw["data"].get("cursor")
            return items, {"cursor": cursor} if cursor else None

        result = await api.get_all("/api/v3/supplies", paginator=paginator)
        assert len(result) == 3
        assert result[0]["id"] == 1


@pytest.mark.unit
class TestPaginationNotSupported:
    async def test_no_list_in_response_raises(self, api: MockedAPI) -> None:
        api.add_response({"status": "ok", "count": 3})
        with pytest.raises(PaginationNotSupported):
            await api.get_all("/api/v3/supplies")

    async def test_empty_first_page_offset_raises(self, api: MockedAPI) -> None:
        api.add_response({"items": []})
        with pytest.raises(PaginationNotSupported):
            await api.get_all("/api/v3/supplies")
