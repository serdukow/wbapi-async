"""Response objects behave as real dicts and lists, with attribute access."""

from __future__ import annotations

import copy
import json
import pickle
from typing import Any

import pytest

from wbapi.types import WBDict, WBList, WBObject, wrap


@pytest.fixture
def resp() -> WBDict:
    return wrap(
        {
            "orders": [
                {"id": 1, "nmID": 55, "options": {"isB2B": True}},
                {"id": 2, "nmID": 66, "options": {"isB2B": False}},
            ],
            "total": 2,
        }
    )


def test_attribute_access(resp: WBDict) -> None:
    assert resp.orders[0].id == 1


def test_nested_attribute_access(resp: WBDict) -> None:
    assert resp.orders[0].options.isB2B is True


def test_missing_key_lists_available(resp: WBDict) -> None:
    with pytest.raises(AttributeError, match="orders"):
        _ = resp.nope


def test_missing_attribute_on_list_explains(resp: WBDict) -> None:
    with pytest.raises(AttributeError, match="list of 2 items"):
        _ = resp.orders.nope


def test_is_a_real_dict(resp: WBDict) -> None:
    assert isinstance(resp, dict)
    assert isinstance(resp, WBObject)


def test_is_a_real_list(resp: WBDict) -> None:
    assert isinstance(resp.orders, list)
    assert isinstance(resp.orders, WBObject)


def test_dict_unpacking_yields_plain_values(resp: WBDict) -> None:
    """Spreading a record must produce plain values, nested ones included."""
    row = {**resp.orders[0]}
    assert row["id"] == 1
    assert type(row["options"]) is dict


def test_json_serialisable(resp: WBDict) -> None:
    assert json.loads(json.dumps(resp)) == {
        "orders": [
            {"id": 1, "nmID": 55, "options": {"isB2B": True}},
            {"id": 2, "nmID": 66, "options": {"isB2B": False}},
        ],
        "total": 2,
    }


def test_list_is_json_serialisable(resp: WBDict) -> None:
    assert json.loads(json.dumps(resp.orders))[0]["id"] == 1


def test_get_returns_default(resp: WBDict) -> None:
    assert resp.get("nope", "fallback") == "fallback"


def test_get_wraps_containers(resp: WBDict) -> None:
    assert resp.get("orders")[0].id == 1


def test_item_access(resp: WBDict) -> None:
    assert resp["total"] == 2
    assert resp["orders"][0].id == 1


def test_contains(resp: WBDict) -> None:
    assert "orders" in resp
    assert "missing" not in resp


def test_len_and_bool(resp: WBDict) -> None:
    assert len(resp.orders) == 2
    assert not wrap([])
    assert not wrap({})


def test_iteration_wraps_items(resp: WBDict) -> None:
    assert [order.id for order in resp.orders] == [1, 2]


def test_sorting_works(resp: WBDict) -> None:
    assert [o.id for o in sorted(resp.orders, key=lambda o: -o.nmID)] == [2, 1]


def test_slicing_returns_wrapped_list(resp: WBDict) -> None:
    first = resp.orders[:1]
    assert isinstance(first, WBList)
    assert first[0].id == 1


def test_list_concatenation(resp: WBDict) -> None:
    assert len(resp.orders + [{"id": 3}]) == 3


def test_values_and_items_are_wrapped(resp: WBDict) -> None:
    assert any(isinstance(v, WBList) for v in resp.values())
    assert dict(resp.items())["total"] == 2


def test_equality_with_plain_data() -> None:
    assert wrap({"a": 1}) == {"a": 1}
    assert wrap([1, 2]) == [1, 2]


def test_copy_and_pickle_round_trip(resp: WBDict) -> None:
    assert copy.deepcopy(resp) == resp
    assert pickle.loads(pickle.dumps(resp)) == resp


@pytest.mark.parametrize(
    ("value", "expected"),
    [(1, int), ("s", str), (True, bool), (None, type(None)), (1.5, float)],
)
def test_scalars_pass_through(value: Any, expected: type) -> None:
    assert type(wrap(value)) is expected


def test_repr_is_truncated() -> None:
    assert len(repr(wrap({"k": "v" * 5000}))) < 300


def test_repr_reads_like_the_data(resp: WBDict) -> None:
    assert repr(resp).startswith("{'orders'")


def test_empty_containers() -> None:
    assert wrap({}) == {}
    assert wrap([]) == []
