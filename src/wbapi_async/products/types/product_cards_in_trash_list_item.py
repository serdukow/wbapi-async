from pydantic import Field

from ...types.base import BaseType
from .characteristics_item import CharacteristicsItem
from .dimensions import Dimensions
from .photos_item import PhotosItem
from .sizes_item import SizesItem
from .wholesale import Wholesale


class ProductCardsInTrashListItem(BaseType):
    """Product Cards in Trash List"""

    nm_id: int | None = Field(None, alias="nmID")
    vendor_code: str | None = Field(None, alias="vendorCode")
    subject_id: int | None = Field(None, alias="subjectID")
    subject_name: str | None = Field(None, alias="subjectName")
    photos: list[PhotosItem] | None = Field(None)
    video: str | None = Field(None)
    wholesale: Wholesale | None = Field(None)
    sizes: list[SizesItem] | None = Field(None)
    dimensions: Dimensions | None = Field(None)
    characteristics: list[CharacteristicsItem] | None = Field(None)
    created_at: str | None = Field(None, alias="createdAt")
    trashed_at: str | None = Field(None, alias="trashedAt")
