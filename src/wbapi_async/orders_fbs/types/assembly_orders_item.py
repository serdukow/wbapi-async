from typing import Any

from pydantic import Field

from ...types.base import BaseType


class AssemblyOrdersItem(BaseType):
    """Get Assembly Orders"""

    address: dict[str, Any] | None = Field(None)
    scan_price: float | None = Field(None, alias="scanPrice")
    delivery_type: str | None = Field(None, alias="deliveryType")
    supply_id: str | None = Field(None, alias="supplyId")
    order_uid: str | None = Field(None, alias="orderUid")
    article: str | None = Field(None)
    color_code: str | None = Field(None, alias="colorCode")
    rid: str | None = Field(None)
    created_at: str | None = Field(None, alias="createdAt")
    offices: list[str] | None = Field(None)
    skus: list[str] | None = Field(None)
    id_: int | None = Field(None, alias="id")
    warehouse_id: int | None = Field(None, alias="warehouseId")
    office_id: int | None = Field(None, alias="officeId")
    nm_id: int | None = Field(None, alias="nmId")
    chrt_id: int | None = Field(None, alias="chrtId")
    price: int | None = Field(None)
    converted_price: int | None = Field(None, alias="convertedPrice")
    currency_code: int | None = Field(None, alias="currencyCode")
    converted_currency_code: int | None = Field(None, alias="convertedCurrencyCode")
    cargo_type: int | None = Field(None, alias="cargoType")
    cross_border_type: int | None = Field(None, alias="crossBorderType")
    comment: str | None = Field(None)
    is_zero_order: bool | None = Field(None, alias="isZeroOrder")
    options: dict[str, Any] | None = Field(None)
