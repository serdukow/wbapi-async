from pydantic import Field

from ...orders_fbs.types.address import Address
from ...types.base import BaseType
from .options_2 import Options2


class NewOrdersItem(BaseType):
    """Get New Orders"""

    address: Address | None = Field(None, alias="address")
    sale_price: int | None = Field(None, alias="salePrice")
    required_meta: list[str] | None = Field(None, alias="requiredMeta")
    comment: str | None = Field(None, alias="comment")
    options: Options2 | None = Field(None, alias="options")
    order_uid: str | None = Field(None, alias="orderUid")
    group_id: str | None = Field(None, alias="groupId")
    article: str | None = Field(None, alias="article")
    color_code: str | None = Field(None, alias="colorCode")
    rid: str | None = Field(None, alias="rid")
    created_at: str | None = Field(None, alias="createdAt")
    skus: list[str] | None = Field(None, alias="skus")
    id_: int | None = Field(None, alias="id")
    warehouse_id: int | None = Field(None, alias="warehouseId")
    nm_id: int | None = Field(None, alias="nmId")
    chrt_id: int | None = Field(None, alias="chrtId")
    price: int | None = Field(None, alias="price")
    converted_price: int | None = Field(None, alias="convertedPrice")
    currency_code: int | None = Field(None, alias="currencyCode")
    converted_currency_code: int | None = Field(None, alias="convertedCurrencyCode")
    cargo_type: int | None = Field(None, alias="cargoType")
    is_zero_order: bool | None = Field(None, alias="isZeroOrder")
