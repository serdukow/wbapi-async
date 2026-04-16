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
    brand: str | None = Field(None, alias="brand")
    title: str | None = Field(None, alias="title")
    description: str | None = Field(None, alias="description")
    need_kiz: bool | None = Field(None, alias="needKiz")
    photos: list[PhotosItem] | None = Field(None, alias="photos")
    video: str | None = Field(None, alias="video")
    wholesale: Wholesale | None = Field(None, alias="wholesale")
    dimensions: Dimensions | None = Field(None, alias="dimensions")
    characteristics: list[CharacteristicsItem] | None = Field(None, alias="characteristics")
    sizes: list[SizesItem] | None = Field(None, alias="sizes")
    tags: list[TagsItem] | None = Field(None, alias="tags")
    created_at: str | None = Field(None, alias="createdAt")
    updated_at: str | None = Field(None, alias="updatedAt")
