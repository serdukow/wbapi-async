from pydantic import Field

from ...types.base import BaseType
from .sizes_item_2 import SizesItem2


class ProductsWithPricesItem(BaseType):
    """Get Products with Prices"""

    nm_id: int | None = Field(None, alias="nmID")
    vendor_code: str | None = Field(None, alias="vendorCode")
    sizes: list[SizesItem2] | None = Field(None, alias="sizes")
    currency_iso_code4217: str | None = Field(None, alias="currencyIsoCode4217")
    discount: int | None = Field(None, alias="discount")
    club_discount: int | None = Field(None, alias="clubDiscount")
    editable_size_price: bool | None = Field(None, alias="editableSizePrice")
    is_bad_turnover: bool | None = Field(None, alias="isBadTurnover")
