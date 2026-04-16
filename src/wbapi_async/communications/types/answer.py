from pydantic import Field

from ...types.base import BaseType


class Answer(BaseType):
    """Answer structure"""

    text: str | None = Field(None)
    editable: bool | None = Field(None)
    create_date: str | None = Field(None, alias="createDate")
