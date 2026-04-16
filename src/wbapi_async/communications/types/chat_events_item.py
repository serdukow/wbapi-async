from pydantic import Field

from ...types.base import BaseType
from .message import Message


class ChatEventsItem(BaseType):
    """Chat Events"""

    chat_id: str | None = Field(None, alias="chatID")
    event_id: str | None = Field(None, alias="eventID")
    event_type: str | None = Field(None, alias="eventType")
    is_new_chat: bool | None = Field(None, alias="isNewChat")
    message: Message | None = Field(None, alias="message")
    source: str | None = Field(None, alias="source")
    add_timestamp: int | None = Field(None, alias="addTimestamp")
    add_time: str | None = Field(None, alias="addTime")
    reply_sign: str | None = Field(None, alias="replySign")
    sender: str | None = Field(None, alias="sender")
    client_name: str | None = Field(None, alias="clientName")
