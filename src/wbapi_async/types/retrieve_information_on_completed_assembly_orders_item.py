from pydantic import Field

from .base import BaseType


class RetrieveInformationOnCompletedAssemblyOrdersItem(BaseType):
    """Retrieve Information on Completed Assembly Orders"""

    article: str | None = Field(None)
    cargo_type: int | None = Field(None, alias="cargoType")
    chrt_id: int | None = Field(None, alias="chrtId")
    created_at: str | None = Field(None, alias="createdAt")
    price: int | None = Field(None)
    final_price: int | None = Field(None, alias="finalPrice")
    converted_price: int | None = Field(None, alias="convertedPrice")
    converted_final_price: int | None = Field(None, alias="convertedFinalPrice")
    currency_code: int | None = Field(None, alias="currencyCode")
    converted_currency_code: int | None = Field(None, alias="convertedCurrencyCode")
    id: int | None = Field(None)
    is_zero_order: bool | None = Field(None, alias="isZeroOrder")
    nm_id: int | None = Field(None, alias="nmId")
    order_code: str | None = Field(None, alias="orderCode")
    pay_mode: str | None = Field(None, alias="payMode")
    rid: str | None = Field(None)
    skus: list[str] | None = Field(None)
    warehouse_address: str | None = Field(None, alias="warehouseAddress")
    warehouse_id: int | None = Field(None, alias="warehouseId")
