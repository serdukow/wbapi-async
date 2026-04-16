from pydantic import Field

from ...types.base import BaseType
from .characteristics_item import CharacteristicsItem
from .dimensions import Dimensions
from .sizes_item import SizesItem
from .wholesale import Wholesale


class CardsToAddItem(BaseType):
    brand: str | None = Field(None, alias="brand")
    vendor_code: str = Field(alias="vendorCode")
    wholesale: Wholesale | None = Field(None, alias="wholesale")
    title: str | None = Field(None, alias="title")
    description: str | None = Field(None, alias="description")
    dimensions: Dimensions | None = Field(None, alias="dimensions")
    sizes: list[SizesItem] | None = Field(None, alias="sizes")
    characteristics: list[CharacteristicsItem] | None = Field(None, alias="characteristics")
