from pydantic import Field

from .base import BaseType


class Size(BaseType):
    size_id: int | None = Field(None, alias="sizeID")
    price: int | None = Field(None, alias="price")
    discounted_price: float | None = Field(None, alias="discountedPrice")
    club_discounted_price: float | None = Field(None, alias="clubDiscountedPrice")
    tech_size_name: str | None = Field(None, alias="techSizeName")
