from pydantic import Field

from ...types.base import BaseType
from ..enums.event_type import EventType
from ..enums.sender import Sender
from .message import Message


class ChatEventsItem(BaseType):
    """Chat Events"""

    chat_id: str | None = Field(None, alias="chatID")
    event_id: str | None = Field(None, alias="eventID")
    event_type: EventType | None = Field(None, alias="eventType")
    is_new_chat: bool | None = Field(None, alias="isNewChat")
    message: Message | None = Field(None)
    source: str | None = Field(None)
    add_timestamp: int | None = Field(None, alias="addTimestamp")
    add_time: str | None = Field(None, alias="addTime")
    reply_sign: str | None = Field(None, alias="replySign")
    sender: Sender | None = Field(None)
    client_name: str | None = Field(None, alias="clientName")
