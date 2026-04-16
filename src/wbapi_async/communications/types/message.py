from pydantic import Field

from ...types.base import BaseType
from .event_attachments import EventAttachments


class Message(BaseType):
    """Message data"""

    attachments: EventAttachments | None = Field(None)
    text: str | None = Field(None)
