from typing import Any

from pydantic import Field

from .base import BaseType


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
    photos: list[dict[str, Any]] | None = Field(None)
    video: str | None = Field(None)
    wholesale: dict[str, Any] | None = Field(None)
    dimensions: dict[str, Any] | None = Field(None)
    characteristics: list[dict[str, Any]] | None = Field(None)
    sizes: list[dict[str, Any]] | None = Field(None)
    tags: list[dict[str, Any]] | None = Field(None)
    created_at: str | None = Field(None, alias="createdAt")
    updated_at: str | None = Field(None, alias="updatedAt")
