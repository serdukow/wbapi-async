from __future__ import annotations

import httpx
import pytest

from tests.conftest import Recorder
from wbapi import WBApi
from wbapi.client import method as method_module


async def test_single_page_by_default(api: WBApi, recorder: Recorder) -> None:
    recorder.add({"orders": [{"id": i} for i in range(10)], "next": 555})
    page = await api.orders_fbs.get_orders(limit=10, next_=0)
    assert len(page.orders) == 10
    assert recorder.count == 1


async def test_auto_paginate_collects_every_page(api: WBApi, recorder: Recorder) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        cursor = request.url.params.get("next")
        if cursor in (None, "0"):
            return httpx.Response(200, json={"orders": [{"id": i} for i in range(1000)], "next": 111})
        if cursor == "111":
            return httpx.Response(200, json={"orders": [{"id": 1001}], "next": 222})
        return httpx.Response(200, json={"orders": [], "next": 0})

    recorder.handle(handler)
    rows = await api.orders_fbs.get_orders(limit=1000, next_=0, auto_paginate=True)
    assert len(rows) == 1001


async def test_iterator_yields_the_same_rows(api: WBApi, recorder: Recorder) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        cursor = request.url.params.get("next")
        if cursor in (None, "0"):
            return httpx.Response(200, json={"orders": [{"id": 1}, {"id": 2}], "next": 9})
        return httpx.Response(200, json={"orders": [], "next": 0})

    recorder.handle(handler)
    rows = [row async for row in api.orders_fbs.iter_get_orders(limit=2, next_=0)]
    assert [row.id for row in rows] == [1, 2]


async def test_next_token_is_sent_back(api: WBApi, recorder: Recorder) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        cursor = request.url.params.get("next")
        if cursor in (None, "0"):
            return httpx.Response(200, json={"orders": [{"id": 1}], "next": 42})
        return httpx.Response(200, json={"orders": [], "next": 0})

    recorder.handle(handler)
    await api.orders_fbs.get_orders(limit=1, next_=0, auto_paginate=True)
    assert recorder.requests[1].url.params["next"] == "42"


async def test_repeated_cursor_stops_the_walk(api: WBApi, recorder: Recorder) -> None:
    """A server repeating the cursor must not loop the walk."""
    recorder.handle(lambda request: httpx.Response(200, json={"orders": [{"id": 1}], "next": 7}))
    rows = await api.orders_fbs.get_orders(limit=1, next_=0, auto_paginate=True)
    assert len(rows) == 2
    assert recorder.count == 2


async def test_empty_page_stops_the_walk(api: WBApi, recorder: Recorder) -> None:
    recorder.handle(lambda request: httpx.Response(200, json={"orders": [], "next": 5}))
    rows = await api.orders_fbs.get_orders(limit=10, next_=0, auto_paginate=True)
    assert rows == []
    assert recorder.count == 1


async def test_skip_take_advances_by_take(api: WBApi, recorder: Recorder) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        skip = int(request.url.params.get("skip", 0))
        rows = [] if skip else [{"id": "f1"}, {"id": "f2"}]
        return httpx.Response(200, json={"data": {"feedbacks": rows}})

    recorder.handle(handler)
    rows = [row async for row in api.communications.iter_get_feedbacks(is_answered=False, take=2, skip=0)]
    assert len(rows) == 2
    assert recorder.requests[1].url.params["skip"] == "2"


async def test_offset_query_advances_by_limit(api: WBApi, recorder: Recorder) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        offset = int(request.url.params.get("offset", 0))
        rows = [] if offset else [{"id": 1}, {"id": 2}]
        return httpx.Response(200, json={"data": rows})

    recorder.handle(handler)
    rows = [row async for row in api.items.iter_get_object_all(limit=2)]
    assert len(rows) == 2
    assert recorder.requests[1].url.params["offset"] == "2"


async def test_runaway_walk_is_aborted(api: WBApi, recorder: Recorder) -> None:
    """A server that never signals the end is stopped by MAX_PAGES."""
    original = method_module.MAX_PAGES
    method_module.MAX_PAGES = 3
    try:
        counter = iter(range(10_000))
        recorder.handle(
            lambda request: httpx.Response(200, json={"orders": [{"id": 1}], "next": next(counter) + 1})
        )
        with pytest.raises(RuntimeError, match=str(3)):
            await api.orders_fbs.get_orders(limit=1, next_=0, auto_paginate=True)
    finally:
        method_module.MAX_PAGES = original


async def test_rows_are_typed(api: WBApi, recorder: Recorder) -> None:
    recorder.add({"orders": [{"id": 1, "nmId": 55}], "next": 0})
    rows = await api.orders_fbs.get_orders(limit=1, next_=0, auto_paginate=True)
    assert rows[0].nm_id == 55


async def test_nested_rows_are_found(api: WBApi, recorder: Recorder) -> None:
    """Rows nested under data.feedbacks must still be found."""
    recorder.handle(
        lambda request: httpx.Response(
            200,
            json={
                "data": {
                    "feedbacks": [] if request.url.params.get("skip") not in (None, "0") else [{"id": "f1"}]
                }
            },
        )
    )
    rows = [row async for row in api.communications.iter_get_feedbacks(is_answered=False, take=1, skip=0)]
    assert len(rows) == 1


async def test_offset_body_advances_in_the_payload(api: WBApi, recorder: Recorder) -> None:
    """Reports carry offset in the body rather than the query string."""
    import json

    from wbapi.client.method import WBMethod

    class Report(WBMethod[list]):
        __path__ = "/api/v2/stocks-report/products/products"
        __http_method__ = "POST"
        __returns__ = list
        __host__ = "https://seller-analytics-api.wildberries.ru"
        __paginate__ = "offset_body"
        __body_fields__ = {"limit": "limit"}

        limit: int = 2

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content or b"{}")
        rows = [] if body.get("offset") else [{"nmID": 1}, {"nmID": 2}]
        return httpx.Response(200, json=rows)

    recorder.handle(handler)
    rows = [row async for row in Report(limit=2).stream(api)]
    assert len(rows) == 2
    assert recorder.body(1)["offset"] == 2
    assert recorder.body(1)["limit"] == 2


async def test_cursor_carries_updated_at_and_nm_id(api: WBApi, recorder: Recorder) -> None:
    """Content v2 continues from the cursor returned in the response."""
    import json

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content or b"{}")
        cursor = body.get("settings", {}).get("cursor", {})
        if cursor.get("updatedAt"):
            return httpx.Response(200, json={"cards": [], "cursor": {"total": 0}})
        return httpx.Response(
            200,
            json={
                "cards": [{"nmID": 1}] * 100,
                "cursor": {"total": 100, "updatedAt": "2026-08-20", "nmID": 99},
            },
        )

    recorder.handle(handler)
    rows = [row async for row in api.items.iter_get_cards_list()]
    assert len(rows) == 100
    second = recorder.body(1)["settings"]["cursor"]
    assert second["updatedAt"] == "2026-08-20"
    assert second["nmID"] == 99


async def test_cursor_stops_without_continuation(api: WBApi, recorder: Recorder) -> None:
    recorder.handle(
        lambda request: httpx.Response(200, json={"cards": [{"nmID": 1}] * 5, "cursor": {"total": 99}})
    )
    rows = [row async for row in api.items.iter_get_cards_list()]
    assert len(rows) == 5
    assert recorder.count == 1


async def test_rrdid_continues_from_the_last_row(api: WBApi, recorder: Recorder) -> None:
    """A finance report continues from the last row's rrdId."""
    import json

    def handler(request: httpx.Request) -> httpx.Response:
        body = json.loads(request.content or b"{}")
        if body.get("rrdId"):
            return httpx.Response(200, json=[])
        return httpx.Response(200, json=[{"rrdId": 77, "quantity": 1}])

    recorder.handle(handler)
    rows = [
        row
        async for row in api.finances.iter_get_acquiring_detailed(
            date_from="2026-08-01", date_to="2026-08-20"
        )
    ]
    assert len(rows) == 1
    assert recorder.body(1)["rrdId"] == 77


async def test_paginate_and_stream_agree(api: WBApi, recorder: Recorder) -> None:
    pages = [
        {"orders": [{"id": 1}, {"id": 2}], "next": 5},
        {"orders": [{"id": 3}], "next": 0},
    ]

    def handler(request: httpx.Request) -> httpx.Response:
        index = 0 if request.url.params.get("next") in (None, "0") else 1
        return httpx.Response(200, json=pages[index])

    recorder.handle(handler)
    collected = await api.orders_fbs.get_orders(limit=2, next_=0, auto_paginate=True)

    recorder.requests.clear()
    streamed = [row async for row in api.orders_fbs.iter_get_orders(limit=2, next_=0)]

    assert [row.id for row in collected] == [row.id for row in streamed] == [1, 2, 3]
