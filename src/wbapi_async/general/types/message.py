from pydantic import Field

from ...types.base import BaseType
from .attachments import Attachments


class Message(BaseType):
    """Message data"""

    attachments: Attachments | None = Field(None)
    text: str | None = Field(None)
