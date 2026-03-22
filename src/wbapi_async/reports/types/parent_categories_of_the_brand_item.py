from pydantic import Field

from ...types.base import BaseType


class ParentCategoriesOfTheBrandItem(BaseType):
    """Parent Categories of the Brand"""

    parent_id: int | None = Field(None, alias="parentId")
    parent_name: str | None = Field(None, alias="parentName")
