from pydantic import Field

from ...types.base import BaseType
from .address import Address
from .options import Options


class AssemblyOrdersItem(BaseType):
    """Get Assembly Orders"""

    address: Address | None = Field(None, alias="address")
    scan_price: float | None = Field(None, alias="scanPrice")
    delivery_type: str | None = Field(None, alias="deliveryType")
    supply_id: str | None = Field(None, alias="supplyId")
    order_uid: str | None = Field(None, alias="orderUid")
    article: str | None = Field(None, alias="article")
    color_code: str | None = Field(None, alias="colorCode")
    rid: str | None = Field(None, alias="rid")
    created_at: str | None = Field(None, alias="createdAt")
    offices: list[str] | None = Field(None, alias="offices")
    skus: list[str] | None = Field(None, alias="skus")
    id_: int | None = Field(None, alias="id")
    warehouse_id: int | None = Field(None, alias="warehouseId")
    office_id: int | None = Field(None, alias="officeId")
    nm_id: int | None = Field(None, alias="nmId")
    chrt_id: int | None = Field(None, alias="chrtId")
    price: int | None = Field(None, alias="price")
    converted_price: int | None = Field(None, alias="convertedPrice")
    currency_code: int | None = Field(None, alias="currencyCode")
    converted_currency_code: int | None = Field(None, alias="convertedCurrencyCode")
    cargo_type: int | None = Field(None, alias="cargoType")
    cross_border_type: int | None = Field(None, alias="crossBorderType")
    comment: str | None = Field(None, alias="comment")
    is_zero_order: bool | None = Field(None, alias="isZeroOrder")
    options: Options | None = Field(None, alias="options")
