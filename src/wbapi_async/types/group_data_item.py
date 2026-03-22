from typing import Any

from pydantic import Field

from .base import BaseType


class GroupDataItem(BaseType):
    """Group Data"""

    subject_id: int = Field(None, alias="subjectID")
    subject_name: str = Field(None, alias="subjectName")
    brand_name: str = Field(None, alias="brandName")
    tag_id: int = Field(None, alias="tagID")
    tag_name: str = Field(None, alias="tagName")
    metrics: Any = Field(None)
    items: list[Any] = Field(None)
