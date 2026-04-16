from pydantic import Field

from ...types.base import BaseType


class Answer(BaseType):
    """Answer structure"""

    text: str | None = Field(None, alias="text")
    editable: bool | None = Field(None, alias="editable")
    create_date: str | None = Field(None, alias="createDate")
