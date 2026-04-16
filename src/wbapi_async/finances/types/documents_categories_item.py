from pydantic import Field

from ...types.base import BaseType


class DocumentsCategoriesItem(BaseType):
    """Documents Categories"""

    name: str | None = Field(None, alias="name")
    title: str | None = Field(None, alias="title")
