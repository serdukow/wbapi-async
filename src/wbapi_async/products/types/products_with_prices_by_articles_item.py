from pydantic import Field

from ...types.base import BaseType
from .sizes_item import SizesItem


class ProductsWithPricesByArticlesItem(BaseType):
    """Get Products with Prices by Articles"""

    nm_id: int | None = Field(None, alias="nmID")
    vendor_code: str | None = Field(None, alias="vendorCode")
    sizes: list[SizesItem] | None = Field(None)
    currency_iso_code4217: str | None = Field(None, alias="currencyIsoCode4217")
    discount: int | None = Field(None)
    club_discount: int | None = Field(None, alias="clubDiscount")
    editable_size_price: bool | None = Field(None, alias="editableSizePrice")
    is_bad_turnover: bool | None = Field(None, alias="isBadTurnover")
