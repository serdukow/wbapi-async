from typing import Any

from pydantic import Field

from .base import BaseType


class ChatListItem(BaseType):
    """Chat List"""

    chat_id: str | None = Field(None, alias="chatID")
    reply_sign: str | None = Field(None, alias="replySign")
    client_name: str | None = Field(None, alias="clientName")
    good_card: dict[str, Any] | None = Field(None, alias="goodCard")
    last_message: Any | None = Field(None, alias="lastMessage")
