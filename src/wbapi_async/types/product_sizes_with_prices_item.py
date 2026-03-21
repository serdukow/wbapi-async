from pydantic import Field

from .base import BaseType


class ProductSizesWithPricesItem(BaseType):
    """Get Product Sizes with Prices"""

    nm_id: int | None = Field(None, alias="nmID")
    size_id: int | None = Field(None, alias="sizeID")
    vendor_code: str | None = Field(None, alias="vendorCode")
    price: int | None = Field(None)
    currency_iso_code4217: str | None = Field(None, alias="currencyIsoCode4217")
    discounted_price: float | None = Field(None, alias="discountedPrice")
    club_discounted_price: float | None = Field(None, alias="clubDiscountedPrice")
    discount: int | None = Field(None)
    club_discount: int | None = Field(None, alias="clubDiscount")
    tech_size_name: str | None = Field(None, alias="techSizeName")
    editable_size_price: bool | None = Field(None, alias="editableSizePrice")
    is_bad_turnover: bool | None = Field(None, alias="isBadTurnover")
