from typing import Any

from pydantic import Field

from ...types.base import BaseType


class NewAssemblyOrdersItem(BaseType):
    """Get New Assembly Orders"""

    address: dict[str, Any] | None = Field(None)
    ddate: str | None = Field(None)
    seller_date: str | None = Field(None, alias="sellerDate")
    sale_price: int | None = Field(None, alias="salePrice")
    required_meta: list[str] | None = Field(None, alias="requiredMeta")
    optional_meta: list[str] | None = Field(None, alias="optionalMeta")
    delivery_type: str | None = Field(None, alias="deliveryType")
    comment: str | None = Field(None)
    scan_price: float | None = Field(None, alias="scanPrice")
    order_uid: str | None = Field(None, alias="orderUid")
    article: str | None = Field(None)
    color_code: str | None = Field(None, alias="colorCode")
    rid: str | None = Field(None)
    created_at: str | None = Field(None, alias="createdAt")
    offices: list[str] | None = Field(None)
    skus: list[str] | None = Field(None)
    id: int | None = Field(None)
    warehouse_id: int | None = Field(None, alias="warehouseId")
    office_id: int | None = Field(None, alias="officeId")
    nm_id: int | None = Field(None, alias="nmId")
    chrt_id: int | None = Field(None, alias="chrtId")
    price: int | None = Field(None)
    final_price: int | None = Field(None, alias="finalPrice")
    converted_price: int | None = Field(None, alias="convertedPrice")
    converted_final_price: int | None = Field(None, alias="convertedFinalPrice")
    currency_code: int | None = Field(None, alias="currencyCode")
    converted_currency_code: int | None = Field(None, alias="convertedCurrencyCode")
    cargo_type: int | None = Field(None, alias="cargoType")
    cross_border_type: int | None = Field(None, alias="crossBorderType")
    is_zero_order: bool | None = Field(None, alias="isZeroOrder")
    options: dict[str, Any] | None = Field(None)
