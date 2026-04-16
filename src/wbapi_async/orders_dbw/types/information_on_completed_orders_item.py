from pydantic import Field

from ...orders_fbs.types.address import Address
from ...products.enums.cargo_type import CargoType
from ...types.base import BaseType
from .options_2 import Options2


class InformationOnCompletedOrdersItem(BaseType):
    """Get Information on Completed Orders"""

    address: Address | None = Field(None)
    options: Options2 | None = Field(None)
    order_uid: str | None = Field(None, alias="orderUid")
    group_id: str | None = Field(None, alias="groupId")
    article: str | None = Field(None)
    color_code: str | None = Field(None, alias="colorCode")
    rid: str | None = Field(None)
    created_at: str | None = Field(None, alias="createdAt")
    skus: list[str] | None = Field(None)
    id_: int | None = Field(None, alias="id")
    warehouse_id: int | None = Field(None, alias="warehouseId")
    nm_id: int | None = Field(None, alias="nmId")
    chrt_id: int | None = Field(None, alias="chrtId")
    price: int | None = Field(None)
    converted_price: int | None = Field(None, alias="convertedPrice")
    currency_code: int | None = Field(None, alias="currencyCode")
    converted_currency_code: int | None = Field(None, alias="convertedCurrencyCode")
    cargo_type: CargoType | None = Field(None, alias="cargoType")
    comment: str | None = Field(None)
    is_zero_order: bool | None = Field(None, alias="isZeroOrder")
