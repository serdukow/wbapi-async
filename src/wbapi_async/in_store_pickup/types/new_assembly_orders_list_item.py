from pydantic import Field

from ...types.base import BaseType


class NewAssemblyOrdersListItem(BaseType):
    """Get New Assembly Orders List"""

    ddate: str | None = Field(None)
    sale_price: int | None = Field(None, alias="salePrice")
    required_meta: list[str] | None = Field(None, alias="requiredMeta")
    article: str | None = Field(None)
    rid: str | None = Field(None)
    created_at: str | None = Field(None, alias="createdAt")
    warehouse_address: str | None = Field(None, alias="warehouseAddress")
    order_code: str | None = Field(None, alias="orderCode")
    pay_mode: str | None = Field(None, alias="payMode")
    skus: list[str] | None = Field(None)
    id: int | None = Field(None)
    warehouse_id: int | None = Field(None, alias="warehouseId")
    nm_id: int | None = Field(None, alias="nmId")
    chrt_id: int | None = Field(None, alias="chrtId")
    price: int | None = Field(None)
    final_price: int | None = Field(None, alias="finalPrice")
    converted_price: int | None = Field(None, alias="convertedPrice")
    converted_final_price: int | None = Field(None, alias="convertedFinalPrice")
    currency_code: int | None = Field(None, alias="currencyCode")
    converted_currency_code: int | None = Field(None, alias="convertedCurrencyCode")
    cargo_type: int | None = Field(None, alias="cargoType")
    is_zero_order: bool | None = Field(None, alias="isZeroOrder")
