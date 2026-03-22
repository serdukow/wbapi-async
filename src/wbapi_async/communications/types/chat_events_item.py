from typing import Any

from pydantic import Field

from ...types.base import BaseType


class ChatEventsItem(BaseType):
    """Chat Events"""

    chat_id: str | None = Field(None, alias="chatID")
    event_id: str | None = Field(None, alias="eventID")
    event_type: str | None = Field(None, alias="eventType")
    is_new_chat: bool | None = Field(None, alias="isNewChat")
    message: dict[str, Any] | None = Field(None)
    source: str | None = Field(None)
    add_timestamp: int | None = Field(None, alias="addTimestamp")
    add_time: str | None = Field(None, alias="addTime")
    reply_sign: str | None = Field(None, alias="replySign")
    sender: str | None = Field(None)
    client_name: str | None = Field(None, alias="clientName")
