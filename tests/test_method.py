from __future__ import annotations

from typing import Any

import httpx
import msgspec
import pytest

from tests.conftest import Recorder
from wbapi import WBApi
from wbapi.client.method import WBMethod, _relax, _rows
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
    with pytest.raises(WBConfigurationError, match="sandbox"):
        Plain().url(sandbox=True)


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


@pytest.mark.parametrize(
    ("raw", "message", "expected"),
    [
        (
            [{"sellerPromo": 0}, {"sellerPromo": 5}],
            "Expected `str | null`, got `int` - at `$[0].sellerPromo`",
            [{"sellerPromo": "0"}, {"sellerPromo": "5"}],
        ),
        (
            [{"rate": 1.5}],
            "Expected `str | null`, got `float` - at `$[0].rate`",
            [{"rate": "1.5"}],
        ),
        (
            {"data": [{"id": 1}]},
            "Expected `object | null`, got `array` - at `$.data`",
            {"data": {"id": 1}},
        ),
        (
            {"data": {"id": 1}},
            "Expected `array | null`, got `object` - at `$.data`",
            {"data": [{"id": 1}]},
        ),
        (
            {"data": []},
            "Expected `object | null`, got `array` - at `$.data`",
            {"data": None},
        ),
        (
            {"outer": {"data": [{"id": 1}]}},
            "Expected `object | null`, got `array` - at `$.outer.data`",
            {"outer": {"data": {"id": 1}}},
        ),
    ],
)
def test_a_drifting_response_is_reshaped(raw: Any, message: str, expected: Any) -> None:
    assert _relax(raw, message) == expected


@pytest.mark.parametrize(
    ("raw", "message"),
    [
        ({"a": 1}, "Object missing required field `p`"),
        ({"a": 1}, "Expected `str`, got `int` - at `$.absent`"),
        ([{"flag": True}], "Expected `str | null`, got `bool` - at `$[0].flag`"),
        ({"data": "text"}, "Expected `object | null`, got `array` - at `$.data`"),
        ({"a": {"b": 1}}, "Expected `object`, got `array` - at `$.a.missing`"),
    ],
)
def test_a_mismatch_it_cannot_reshape_is_declined(raw: Any, message: str) -> None:
    assert _relax(raw, message) is None


def test_every_row_is_reshaped_not_just_the_reported_one() -> None:
    raw = [{"n": 1}, {"n": 2}, {"n": 3}]

    assert _relax(raw, "Expected `str | null`, got `int` - at `$[0].n`") == [
        {"n": "1"},
        {"n": "2"},
        {"n": "3"},
    ]


def test_a_row_without_the_field_is_left_alone() -> None:
    raw = [{"n": 1}, {"other": 2}]

    assert _relax(raw, "Expected `str | null`, got `int` - at `$[0].n`") == [
        {"n": "1"},
        {"other": 2},
    ]


def test_a_required_body_is_sent_even_when_empty() -> None:
    """WB answers 400 IncorrectRequestBody when a required body is absent.

    create_supply takes only an optional name, so calling it without one used
    to send no body at all.
    """
    from wbapi.orders_fbs.methods import CreateSupply

    assert CreateSupply()._body() == {}
    assert CreateSupply(name="Июнь")._body() == {"name": "Июнь"}


def test_a_method_without_a_body_sends_none() -> None:
    from wbapi.orders_fbs.methods import GetOrdersNew

    assert GetOrdersNew()._body() is None
