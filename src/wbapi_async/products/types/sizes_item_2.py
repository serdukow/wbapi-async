from pydantic import Field

from ...types.base import BaseType


class SizesItem2(BaseType):
    size_id: int = Field(alias="sizeID")
    price: int = Field(alias="price")
    discounted_price: float = Field(alias="discountedPrice")
    club_discounted_price: float = Field(alias="clubDiscountedPrice")
    tech_size_name: str = Field(alias="techSizeName")
