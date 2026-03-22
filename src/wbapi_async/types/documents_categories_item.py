from pydantic import Field

from .base import BaseType


class DocumentsCategoriesItem(BaseType):
    """Documents Categories"""

    name: str | None = Field(None)
    title: str | None = Field(None)
