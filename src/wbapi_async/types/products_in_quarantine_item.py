from pydantic import Field

from .base import BaseType


class ProductsInQuarantineItem(BaseType):
    """Get Products in Quarantine"""

    nm_id: int | None = Field(None, alias="nmID")
    size_id: int | None = Field(None, alias="sizeID")
    tech_size_name: str | None = Field(None, alias="techSizeName")
    currency_iso_code4217: str | None = Field(None, alias="currencyIsoCode4217")
    new_price: float | None = Field(None, alias="newPrice")
    old_price: float | None = Field(None, alias="oldPrice")
    new_discount: int | None = Field(None, alias="newDiscount")
    old_discount: int | None = Field(None, alias="oldDiscount")
    price_diff: float | None = Field(None, alias="priceDiff")
