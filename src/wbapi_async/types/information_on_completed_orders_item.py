from typing import Any

from pydantic import Field

from .base import BaseType


class InformationOnCompletedOrdersItem(BaseType):
    """Get Information on Completed Orders"""

    address: dict[str, Any] | None = Field(None)
    delivery_type: str | None = Field(None, alias="deliveryType")
    options: dict[str, Any] | None = Field(None)
    order_uid: str | None = Field(None, alias="orderUid")
    group_id: str | None = Field(None, alias="groupId")
    article: str | None = Field(None)
    color_code: str | None = Field(None, alias="colorCode")
    rid: str | None = Field(None)
    created_at: str | None = Field(None, alias="createdAt")
    skus: list[str] | None = Field(None)
    id: int | None = Field(None)
    warehouse_id: int | None = Field(None, alias="warehouseId")
    nm_id: int | None = Field(None, alias="nmId")
    chrt_id: int | None = Field(None, alias="chrtId")
    scan_price: int | None = Field(None, alias="scanPrice")
    price: int | None = Field(None)
    converted_price: int | None = Field(None, alias="convertedPrice")
    currency_code: int | None = Field(None, alias="currencyCode")
    converted_currency_code: int | None = Field(None, alias="convertedCurrencyCode")
    converted_final_price: int | None = Field(None, alias="convertedFinalPrice")
    final_price: int | None = Field(None, alias="finalPrice")
    cargo_type: int | None = Field(None, alias="cargoType")
    comment: str | None = Field(None)
    is_zero_order: bool | None = Field(None, alias="isZeroOrder")
    wb_sticker_id: int | None = Field(None, alias="wbStickerId")
