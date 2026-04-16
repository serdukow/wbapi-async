from pydantic import Field

from ...types.base import BaseType


class LastMessage(BaseType):
    """The last message in the chat"""

    text: str | None = Field(None, alias="text")
    add_timestamp: int | None = Field(None, alias="addTimestamp")
