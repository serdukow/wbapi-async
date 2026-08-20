"""Pagination: strategy detection, traversal, and loop safety."""

from __future__ import annotations

import json as jsonlib
from typing import Any

import httpx
import pytest

from tests.mocked_api import MockedAPI
from wbapi import WBObject
from wbapi.pagination import extract_items


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ([1, 2], [1, 2]),
        ({"data": [1]}, [1]),
        ({"orders": [1]}, [1]),
        ({"nested": {"cards": [1]}}, [1]),
        ({}, []),
        ({"count": 3}, []),
        ("string", []),
        (None, []),
    ],
)
def test_extract_items_finds_the_payload(raw: Any, expected: list[Any]) -> None:
    assert extract_items(raw) == expected


def test_extract_items_skips_diagnostic_lists() -> None:
    """Regression: an empty ``errors`` list used to be mistaken for the payload."""
    assert extract_items({"errors": [], "data": [{"id": 1}]}) == [{"id": 1}]


def test_extract_items_prefers_known_payload_keys() -> None:
    assert extract_items({"warnings": ["w"], "cards": [{"id": 1}]}) == [{"id": 1}]


async def test_offset_pagination_walks_pages(api: MockedAPI) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        offset = int(request.url.params.get("offset", 0))
        if offset == 0:
            return httpx.Response(200, json={"supplies": [{"id": i} for i in range(1000)]})
        return httpx.Response(200, json={"supplies": [{"id": 9999}]})

    api.set_handler(handler)
    items = [item async for item in api.paginate("/api/v3/supplies")]
    assert len(items) == 1001
    assert items[-1].id == 9999


async def test_offset_stops_on_short_page(api: MockedAPI) -> None:
    api.add_response({"supplies": [{"id": 1}]})
    items = [item async for item in api.paginate("/api/v3/supplies")]
    assert len(items) == 1
    assert api.request_count == 1


async def test_next_token_pagination(api: MockedAPI) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.params.get("next") is None:
            return httpx.Response(200, json={"orders": [{"id": 1}], "next": "abc"})
        return httpx.Response(200, json={"orders": [{"id": 2}], "next": 0})

    api.set_handler(handler)
    items = [item async for item in api.paginate("/api/v3/orders")]
    assert [item.id for item in items] == [1, 2]


async def test_next_token_stops_on_repeated_cursor(api: MockedAPI) -> None:
    """A server echoing the same cursor must not spin forever."""
    api.set_handler(lambda request: httpx.Response(200, json={"orders": [{"id": 1}], "next": "same"}))
    items = [item async for item in api.paginate("/api/v3/orders")]
    assert len(items) == 2
    assert api.request_count == 2


async def test_cursor_pagination_for_cards(api: MockedAPI) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if '"updatedAt"' in request.content.decode():
            return httpx.Response(200, json={"cards": [{"nmID": 2}], "cursor": {"total": 1}})
        return httpx.Response(
            200,
            json={
                "cards": [{"nmID": 1}] * 100,
                "cursor": {"total": 100, "updatedAt": "2026-01-01", "nmID": 1},
            },
        )

    api.set_handler(handler)
    items = [
        item async for item in api.paginate("/content/v2/get/cards/list", body={"settings": {"filter": {}}})
    ]
    assert len(items) == 101


async def test_cursor_preserves_caller_settings(api: MockedAPI) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        body = request.content.decode()
        if '"updatedAt"' in body:
            assert '"withPhoto"' in body, "caller filter was dropped on page 2"
            return httpx.Response(200, json={"cards": [], "cursor": {"total": 0}})
        return httpx.Response(
            200,
            json={
                "cards": [{"nmID": 1}] * 100,
                "cursor": {"total": 100, "updatedAt": "t", "nmID": 1},
            },
        )

    api.set_handler(handler)
    [
        item
        async for item in api.paginate(
            "/content/v2/get/cards/list",
            body={"settings": {"filter": {"withPhoto": -1}}},
        )
    ]
    assert api.request_count == 2


async def test_rrdid_pagination_via_query(api: MockedAPI) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.params.get("rrdid") is None:
            return httpx.Response(200, json=[{"rrd_id": 5, "v": "a"}])
        return httpx.Response(200, json=[])

    api.set_handler(handler)
    items = [item async for item in api.paginate("/api/v5/supplier/reportDetailByPeriod")]
    assert [item.v for item in items] == ["a"]


async def test_body_offset_pagination(api: MockedAPI) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        offset = jsonlib.loads(request.content)["offset"]
        if offset == 0:
            return httpx.Response(200, json={"data": [{"i": n} for n in range(1000)]})
        return httpx.Response(200, json={"data": []})

    api.set_handler(handler)
    items = [
        item async for item in api.paginate("/api/v2/stocks-report/products/products", body={"filter": {}})
    ]
    assert len(items) == 1000


async def test_items_are_wrapped(api: MockedAPI) -> None:
    api.add_response({"supplies": [{"id": 1}]})
    items = [item async for item in api.paginate("/api/v3/supplies")]
    assert isinstance(items[0], WBObject)


async def test_empty_result_yields_nothing(api: MockedAPI) -> None:
    api.add_response({"supplies": []})
    assert [item async for item in api.paginate("/api/v3/supplies")] == []


async def test_page_size_override_is_sent(api: MockedAPI) -> None:
    api.add_response({"supplies": []})
    [item async for item in api.paginate("/api/v3/supplies", page_size=7)]
    assert api.get_last_request().url.params["limit"] == "7"


async def test_endpoint_page_size_is_used(api: MockedAPI) -> None:
    api.add_response({"cards": [], "cursor": {"total": 0}})
    [item async for item in api.paginate("/content/v2/get/cards/list", body={})]
    assert jsonlib.loads(api.get_last_request().content)["limit"] == 100


async def test_query_params_survive_pagination(api: MockedAPI) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        assert request.url.params.get("dateFrom") == "2026-01-01"
        return httpx.Response(200, json={"supplies": []})

    api.set_handler(handler)
    [item async for item in api.paginate("/api/v3/supplies", params={"dateFrom": "2026-01-01"})]
    assert api.request_count == 1


async def test_interpolated_path_in_paginate(api: MockedAPI) -> None:
    api.add_response({"trbxes": []})
    [item async for item in api.paginate("/api/v3/supplies/WB-1/trbx")]
    assert api.get_last_request().url.path == "/api/v3/supplies/WB-1/trbx"


async def test_runaway_pagination_is_stopped(api: MockedAPI) -> None:
    """A server that never signals the end must not loop indefinitely."""
    from wbapi import pagination

    original = pagination.MAX_PAGES
    pagination.MAX_PAGES = 5
    try:
        api.set_handler(lambda request: httpx.Response(200, json={"supplies": [{"id": 1}] * 1000}))
        with pytest.raises(RuntimeError, match="exceeded"):
            [item async for item in api.paginate("/api/v3/supplies")]
    finally:
        pagination.MAX_PAGES = original
