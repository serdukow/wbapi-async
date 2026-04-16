from pydantic import Field

from ...types.base import BaseType
from .characteristics_item import CharacteristicsItem
from .dimensions import Dimensions
from .sizes_item import SizesItem
from .wholesale import Wholesale


class CardsToAddItem(BaseType):
    brand: str | None = Field(None)
    vendor_code: str = Field(alias="vendorCode")
    wholesale: Wholesale | None = Field(None)
    title: str | None = Field(None)
    description: str | None = Field(None)
    dimensions: Dimensions | None = Field(None)
    sizes: list[SizesItem] | None = Field(None)
    characteristics: list[CharacteristicsItem] | None = Field(None)
