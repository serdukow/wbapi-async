from typing import Any

from pydantic import Field

from ...types.base import BaseType


class GroupDataItem(BaseType):
    """Group Data"""

    subject_id: int = Field(alias="subjectID")
    subject_name: str = Field(alias="subjectName")
    brand_name: str = Field(alias="brandName")
    tag_id: int = Field(alias="tagID")
    tag_name: str = Field(alias="tagName")
    metrics: Any = Field()
    items: list[Any] = Field()
