from __future__ import annotations

import msgspec
import pytest

from wbapi.client.method import _keep_extras
from wbapi.client.model import WBModel, collect_extras
from wbapi.orders_fbs.models import GetOrdersNewResponse, OrderNew


class Conversions(WBModel):
    add_to_cart_percent: int | None = msgspec.field(default=None, name="addToCartPercent")


class Selected(WBModel):
    conversions: Conversions | None = msgspec.field(default=None)
    orders_count: int | None = msgspec.field(default=None, name="ordersCount")


class Size(WBModel):
    tech_size: str | None = msgspec.field(default=None, name="techSize")


class Product(WBModel):
    nm_id: int | None = msgspec.field(default=None, name="nmId")
    selected: Selected | None = msgspec.field(default=None)
    sizes: list[Size] | None = msgspec.field(default=None)


def decode(raw: dict, struct: type = Product):
    model = msgspec.convert(raw, struct, strict=False)
    _keep_extras(raw, model)
    return model


def test_known_response_has_no_extras() -> None:
    product = decode({"nmId": 1, "selected": {"ordersCount": 5}})
    assert product.extras is None


def test_new_field_is_kept() -> None:
    product = decode({"nmId": 1, "statusFromWb": "SOLD"})
    assert product.extras == {"statusFromWb": "SOLD"}


def test_new_field_is_hidden_by_default() -> None:
    product = decode({"nmId": 1, "statusFromWb": "SOLD"})
    assert "statusFromWb" not in product.to_dict()


def test_new_field_can_be_asked_for() -> None:
    product = decode({"nmId": 1, "statusFromWb": "SOLD"})
    assert product.to_dict(extra=True)["statusFromWb"] == "SOLD"


def test_new_field_sits_next_to_the_described_ones() -> None:
    data = decode({"nmId": 1, "statusFromWb": "SOLD"}).to_dict(extra=True)
    assert data == {"nm_id": 1, "statusFromWb": "SOLD"}


def test_new_field_deep_inside_is_kept() -> None:
    raw = {"nmId": 1, "selected": {"ordersCount": 5, "conversions": {"newMetric": 99}}}
    data = decode(raw).to_dict(extra=True)
    assert data["selected"]["conversions"]["newMetric"] == 99


def test_new_fields_on_several_levels() -> None:
    raw = {"nmId": 1, "top": "a", "selected": {"ordersCount": 5, "deep": "b"}}
    data = decode(raw).to_dict(extra=True)
    assert data["top"] == "a"
    assert data["selected"]["deep"] == "b"


def test_new_field_inside_a_list_item() -> None:
    raw = {"nmId": 1, "sizes": [{"techSize": "M"}, {"techSize": "L", "newSizeField": "x"}]}
    data = decode(raw).to_dict(extra=True)
    assert data["sizes"][1]["newSizeField"] == "x"
    assert "newSizeField" not in data["sizes"][0]


def test_described_fields_survive_alongside_new_ones() -> None:
    raw = {"nmId": 1, "selected": {"ordersCount": 5, "deep": "b"}}
    data = decode(raw).to_dict(extra=True)
    assert data["nm_id"] == 1
    assert data["selected"]["orders_count"] == 5


def test_extras_never_leak_into_the_dict() -> None:
    product = decode({"nmId": 1, "statusFromWb": "SOLD"})
    assert "extras" not in product.to_dict()
    assert "__extras__" not in product.to_dict(extra=True)


def test_extras_are_absent_from_api_names_too() -> None:
    product = decode({"nmId": 1, "statusFromWb": "SOLD"})
    assert "__extras__" not in product.to_dict(by_alias=True)


def test_extras_do_not_reach_json() -> None:
    product = decode({"nmId": 1, "statusFromWb": "SOLD"})
    assert b"__extras__" not in product.to_json()


def test_a_generated_model_collects_extras() -> None:
    order = decode({"id": 1, "nmId": 55, "brandNewField": "x"}, OrderNew)
    assert order.to_dict(extra=True)["brandNewField"] == "x"


def test_extras_inside_a_generated_response() -> None:
    raw = {"orders": [{"id": 1, "nmId": 55, "brandNewField": "x"}]}
    response = decode(raw, GetOrdersNewResponse)
    data = response.to_dict(extra=True)
    assert data["orders"][0]["brandNewField"] == "x"


def test_collect_returns_nothing_when_everything_is_described() -> None:
    assert collect_extras({"nmId": 1, "selected": {"ordersCount": 5}}, Product) is None


def test_collect_keeps_the_path_to_the_field() -> None:
    raw = {"nmId": 1, "selected": {"ordersCount": 5, "deep": "b"}}
    assert collect_extras(raw, Product) == {"selected": {"deep": "b"}}


def test_collect_survives_an_unexpected_shape() -> None:
    assert collect_extras("не объект", Product) is None
    assert collect_extras({"nmId": 1, "selected": "строка вместо объекта"}, Product) is None


def test_keep_extras_never_raises() -> None:
    model = msgspec.convert({"nmId": 1}, Product, strict=False)
    _keep_extras("совсем не то, что ожидалось", model)
    assert model.extras is None


@pytest.mark.parametrize("value", [0, "", False, []])
def test_falsy_values_are_kept(value: object) -> None:
    product = decode({"nmId": 1, "newField": value})
    assert product.to_dict(extra=True)["newField"] == value
