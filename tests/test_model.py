from __future__ import annotations

import json

import msgspec
import pytest

from wbapi.client.model import WBModel
from wbapi.orders_fbs.models import GetOrdersNewResponse, OrderNew


@pytest.fixture
def order() -> OrderNew:
    return msgspec.convert(
        {"id": 13833711, "nmId": 55, "salePrice": 149900, "createdAt": "2026-08-20"},
        OrderNew,
        strict=False,
    )


def test_to_dict_uses_snake_case(order: OrderNew) -> None:
    data = order.to_dict()
    assert data["nm_id"] == 55
    assert data["sale_price"] == 149900


def test_to_dict_skips_empty_fields(order: OrderNew) -> None:
    assert "comment" not in order.to_dict()


def test_to_dict_can_keep_empty_fields(order: OrderNew) -> None:
    assert "comment" in order.to_dict(skip_none=False)


def test_to_dict_can_use_api_names(order: OrderNew) -> None:
    """An existing warehouse schema expects the Wildberries field names."""
    data = order.to_dict(by_alias=True)
    assert data["nmId"] == 55
    assert "nm_id" not in data


def test_to_dict_result_is_a_plain_dict(order: OrderNew) -> None:
    data = order.to_dict()
    assert type(data) is dict
    assert json.dumps(data)


def test_unpacking_into_a_row(order: OrderNew) -> None:
    """The common loading pattern: spread a row and add your own fields."""
    row = {**order.to_dict(), "loaded_at": "2026-08-20"}
    assert row["id"] == 13833711
    assert row["loaded_at"] == "2026-08-20"


def test_nested_structures_become_plain() -> None:
    response = msgspec.convert({"orders": [{"id": 1, "nmId": 55}]}, GetOrdersNewResponse, strict=False)
    data = response.to_dict()
    assert type(data["orders"][0]) is dict
    assert data["orders"][0]["nm_id"] == 55


def test_to_json_uses_api_names(order: OrderNew) -> None:
    assert b'"nmId"' in order.to_json()


def test_from_dict_round_trip(order: OrderNew) -> None:
    restored = OrderNew.from_dict(order.to_dict(by_alias=True))
    assert restored.nm_id == order.nm_id
    assert restored.sale_price == order.sale_price


def test_from_dict_tolerates_extra_fields() -> None:
    """A new field from Wildberries must not break decoding."""
    restored = OrderNew.from_dict({"id": 1, "совсем": "новое"})
    assert restored.id == 1


def test_from_dict_converts_scalars() -> None:
    assert OrderNew.from_dict({"id": "13833711"}).id == 13833711


def test_plain_unwraps_a_nested_struct() -> None:
    """A struct that is not a WBModel still has to become a dict."""

    class Inner(msgspec.Struct):
        value: int = 1

    class Outer(WBModel):
        inner: Inner | None = msgspec.field(default=None)

    data = Outer(inner=Inner()).to_dict()
    assert data["inner"] == {"value": 1}


def test_plain_unwraps_a_dict_of_models() -> None:
    class Item(WBModel):
        name: str | None = msgspec.field(default=None)

    class Outer(WBModel):
        mapping: dict[str, Item] | None = msgspec.field(default=None)

    data = Outer(mapping={"a": Item(name="x")}).to_dict()
    assert data["mapping"] == {"a": {"name": "x"}}


def test_plain_unwraps_a_list_of_models() -> None:
    class Item(WBModel):
        name: str | None = msgspec.field(default=None)

    class Outer(WBModel):
        items: list[Item] | None = msgspec.field(default=None)

    data = Outer(items=[Item(name="x"), Item(name="y")]).to_dict()
    assert data["items"] == [{"name": "x"}, {"name": "y"}]


def test_to_json_can_use_snake_case() -> None:
    class Item(WBModel):
        nm_id: int | None = msgspec.field(default=None, name="nmId")

    assert b"nm_id" in Item(nm_id=1).to_json(by_alias=False)
