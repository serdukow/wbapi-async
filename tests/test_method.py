from __future__ import annotations

from typing import Any

import httpx
import msgspec
import pytest

from tests.conftest import Recorder
from wbapi import WBApi
from wbapi.client.method import WBMethod, _relax_shape, _rows
from wbapi.exceptions import WBConfigurationError


class Row(msgspec.Struct):
    rrd_id: int | None = msgspec.field(default=None, name="rrdId")
    value: str | None = None


class Report(WBMethod[list[Row]]):
    __path__ = "/api/finance/v1/sales-reports/detailed"
    __http_method__ = "POST"
    __returns__ = list[Row]
    __host__ = "https://finance-api.wildberries.ru"
    __paginate__ = "rrdid"


class Plain(WBMethod[None]):
    __path__ = "/api/v3/orders/new"
    __http_method__ = "GET"
    __returns__ = None
    __host__ = "https://marketplace-api.wildberries.ru"


async def test_rrdid_walk_continues_from_the_last_row(api: WBApi, recorder: Recorder) -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        if b"rrdId" in request.content:
            return httpx.Response(200, json=[])
        return httpx.Response(200, json=[{"rrdId": 11, "value": "a"}])

    recorder.handle(handler)
    rows = await Report().paginate(api)
    assert [row.value for row in rows] == ["a"]
    assert recorder.body(1) == {"rrdId": 11}


async def test_rrdid_walk_stops_on_a_repeated_id(api: WBApi, recorder: Recorder) -> None:
    recorder.handle(lambda request: httpx.Response(200, json=[{"rrdId": 7, "value": "x"}]))
    rows = await Report().paginate(api)
    assert len(rows) == 2
    assert recorder.count == 2


async def test_rrdid_walk_stops_without_an_id(api: WBApi, recorder: Recorder) -> None:
    recorder.handle(lambda request: httpx.Response(200, json=[{"value": "no id"}]))
    rows = await Report().paginate(api)
    assert len(rows) == 1
    assert recorder.count == 1


async def test_method_without_pagination_yields_nothing_extra(api: WBApi, recorder: Recorder) -> None:
    recorder.add({"orders": [{"id": 1}]})
    rows = [row async for row in Plain().stream(api)]
    assert rows == []
    assert recorder.count == 1


async def test_sandbox_url_is_refused_without_a_sandbox_host() -> None:
    with pytest.raises(WBConfigurationError, match="песочниц"):
        Plain().url(sandbox=True)


@pytest.mark.parametrize(
    ("raw", "message"),
    [
        ({"a": 1}, "no shape mismatch here"),
        ("not a dict", "Expected `object | null`, got `array` - at `$.data`"),
        ({"other": 1}, "Expected `object | null`, got `array` - at `$.data`"),
        ({"data": "text"}, "Expected `object | null`, got `array` - at `$.data`"),
        ({"a": {"b": 1}}, "Expected `object | null`, got `array` - at `$.a.missing`"),
    ],
)
def test_relax_shape_declines_what_it_cannot_fix(raw: Any, message: str) -> None:
    assert _relax_shape(raw, message) is None


def test_relax_shape_unwraps_a_single_item_array() -> None:
    patched = _relax_shape({"data": [{"id": 1}]}, "Expected `object | null`, got `array` - at `$.data`")
    assert patched == {"data": {"id": 1}}


def test_relax_shape_wraps_an_object_into_an_array() -> None:
    patched = _relax_shape({"data": {"id": 1}}, "Expected `array | null`, got `object` - at `$.data`")
    assert patched == {"data": [{"id": 1}]}


def test_relax_shape_handles_an_empty_array() -> None:
    patched = _relax_shape({"data": []}, "Expected `object | null`, got `array` - at `$.data`")
    assert patched == {"data": None}


def test_relax_shape_reaches_a_nested_field() -> None:
    patched = _relax_shape(
        {"outer": {"data": [{"id": 1}]}},
        "Expected `object | null`, got `array` - at `$.outer.data`",
    )
    assert patched == {"outer": {"data": {"id": 1}}}


@pytest.mark.parametrize(
    ("page", "field", "expected"),
    [
        (None, None, []),
        ([1, 2], None, [1, 2]),
        ("string", None, []),
        (42, "data", []),
    ],
)
def test_rows_handles_odd_pages(page: Any, field: str | None, expected: list) -> None:
    assert _rows(page, field) == expected


def test_rate_limit_without_declared_limits() -> None:
    assert Plain().rate_limit("personal") is None


def test_rate_limit_falls_back_to_any_category() -> None:
    class Limited(WBMethod[None]):
        __path__ = "/x"
        __http_method__ = "GET"
        __returns__ = None
        __host__ = "https://marketplace-api.wildberries.ru"
        __rate_limits__ = {"basic": (60_000, 1)}

    assert Limited().rate_limit("personal") == (60_000, 1)
    assert Limited().rate_limit(None) == (60_000, 1)
