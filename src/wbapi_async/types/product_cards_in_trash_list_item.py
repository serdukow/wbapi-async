from typing import Any

from pydantic import Field

from .base import BaseType


class ProductCardsInTrashListItem(BaseType):
    """Product Cards in Trash List"""

    nm_id: int | None = Field(None, alias="nmID")
    vendor_code: str | None = Field(None, alias="vendorCode")
    subject_id: int | None = Field(None, alias="subjectID")
    subject_name: str | None = Field(None, alias="subjectName")
    photos: list[dict[str, Any]] | None = Field(None)
    video: str | None = Field(None)
    wholesale: dict[str, Any] | None = Field(None)
    sizes: list[dict[str, Any]] | None = Field(None)
    dimensions: dict[str, Any] | None = Field(None)
    characteristics: list[dict[str, Any]] | None = Field(None)
    created_at: str | None = Field(None, alias="createdAt")
    trashed_at: str | None = Field(None, alias="trashedAt")
