from pydantic import Field

from ...types.base import BaseType
from .characteristics_item import CharacteristicsItem
from .dimensions import Dimensions
from .photos_item import PhotosItem
from .sizes_item import SizesItem
from .tags_item import TagsItem
from .wholesale import Wholesale


class ProductCardsListItem(BaseType):
    """Product Cards List"""

    nm_id: int | None = Field(None, alias="nmID")
    imt_id: int | None = Field(None, alias="imtID")
    nm_uuid: str | None = Field(None, alias="nmUUID")
    subject_id: int | None = Field(None, alias="subjectID")
    subject_name: str | None = Field(None, alias="subjectName")
    vendor_code: str | None = Field(None, alias="vendorCode")
    brand: str | None = Field(None)
    title: str | None = Field(None)
    description: str | None = Field(None)
    need_kiz: bool | None = Field(None, alias="needKiz")
    photos: list[PhotosItem] | None = Field(None)
    video: str | None = Field(None)
    wholesale: Wholesale | None = Field(None)
    dimensions: Dimensions | None = Field(None)
    characteristics: list[CharacteristicsItem] | None = Field(None)
    sizes: list[SizesItem] | None = Field(None)
    tags: list[TagsItem] | None = Field(None)
    created_at: str | None = Field(None, alias="createdAt")
    updated_at: str | None = Field(None, alias="updatedAt")
