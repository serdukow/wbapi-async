from __future__ import annotations

import httpx

from tests.conftest import Recorder
from wbapi import WBApi


async def test_item_returns_hits_the_new_path_with_its_filters(api: WBApi, recorder: Recorder) -> None:
    recorder.add(
        {
            "count": 1,
            "report": [{"srid": "s1", "sku": "123", "nmId": 7, "returnStatus": "active", "kiz": "k"}],
        }
    )
    result = await api.reports.get_analytics_item_returns(
        date_from="2026-10-01", date_to="2026-10-02", status="active", limit=10, offset=0
    )

    request = recorder.last
    assert request.method == "GET"
    assert request.url.path == "/api/analytics/v1/item-returns"
    assert request.url.params["dateFrom"] == "2026-10-01"
    assert request.url.params["dateTo"] == "2026-10-02"
    assert request.url.params["status"] == "active"
    assert result.count == 1
    row = result.report[0]
    assert (row.srid, row.sku, row.nm_id, row.return_status, row.kiz) == ("s1", "123", 7, "active", "k")


async def test_item_returns_auto_paginate_walks_offsets(api: WBApi, recorder: Recorder) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        offset = int(request.url.params.get("offset", 0))
        rows = [] if offset else [{"srid": "a"}, {"srid": "b"}]
        return httpx.Response(200, json={"count": 2, "report": rows})

    recorder.handle(handler)
    rows = await api.reports.get_analytics_item_returns(
        date_from="2026-10-01", date_to="2026-10-02", limit=2, auto_paginate=True
    )

    assert [row.srid for row in rows] == ["a", "b"]
    assert recorder.requests[1].url.params["offset"] == "2"
