from pydantic import Field

from .base import BaseType


class Size(BaseType):
    size_id: int | None = Field(None, alias="sizeID")
    price: int | None = Field(None, alias="price")
    discounted_price: float | None = Field(None, alias="discountedPrice")
    club_discounted_price: float | None = Field(None, alias="clubDiscountedPrice")
    tech_size_name: str | None = Field(None, alias="techSizeName")


class ProductWithPrice(BaseType):
    nm_id: int | None = Field(None, alias="nmID")
    vendor_code: str | None = Field(None, alias="vendorCode")
    sizes: list[Size] | None = Field(None, alias="sizes")
    currency_iso_code_4217: str | None = Field(None, alias="currencyIsoCode4217")
    discount: int | None = Field(None, alias="discount")
    club_discount: int | None = Field(None, alias="clubDiscount")
    editable_size_price: bool | None = Field(None, alias="editableSizePrice")
    is_bad_turnover: bool | None = Field(None, alias="isBadTurnover")
