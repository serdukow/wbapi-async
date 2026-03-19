from typing import Any

from pydantic import Field

from .base import BaseType


class ProductCardPhoto(BaseType):
    big: str | None = Field(None, alias="big")
    c246x328: str | None = Field(None, alias="c246x328")
    c516x688: str | None = Field(None, alias="c516x688")
    square: str | None = Field(None, alias="square")
    tm: str | None = Field(None, alias="tm")


class ProductCardWholesale(BaseType):
    enabled: bool | None = Field(None, alias="enabled")
    quantum: int | None = Field(None, alias="quantum")


class ProductCardDimensions(BaseType):
    length: int | None = Field(None, alias="length")
    width: int | None = Field(None, alias="width")
    height: int | None = Field(None, alias="height")
    weight_brutto: float | None = Field(None, alias="weightBrutto")
    is_valid: bool | None = Field(None, alias="isValid")


class ProductCardCharacteristic(BaseType):
    id: int | None = Field(None, alias="id")
    name: str | None = Field(None, alias="name")
    value: Any | None = Field(None, alias="value")


class ProductCardSize(BaseType):
    chrt_id: int | None = Field(None, alias="chrtID")
    tech_size: str | None = Field(None, alias="techSize")
    skus: list[str] | None = Field(None, alias="skus")


class ProductCardTag(BaseType):
    id: int | None = Field(None, alias="id")
    name: str | None = Field(None, alias="name")
    color: str | None = Field(None, alias="color")


class ProductCard(BaseType):
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
    photos: list[ProductCardPhoto] | None = Field(None, alias="photos")
    video: str | None = Field(None, alias="video")
    wholesale: ProductCardWholesale | None = Field(None, alias="wholesale")
    dimensions: ProductCardDimensions | None = Field(None, alias="dimensions")
    characteristics: list[ProductCardCharacteristic] | None = Field(None, alias="characteristics")
    sizes: list[ProductCardSize] | None = Field(None, alias="sizes")
    tags: list[ProductCardTag] | None = Field(None, alias="tags")
    created_at: str | None = Field(None, alias="createdAt")
    updated_at: str | None = Field(None, alias="updatedAt")
