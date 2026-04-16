from pydantic import Field

from ...types.base import BaseType
from .good_card import GoodCard
from .last_message import LastMessage


class ChatListItem(BaseType):
    """Chat List"""

    chat_id: str | None = Field(None, alias="chatID")
    reply_sign: str | None = Field(None, alias="replySign")
    client_name: str | None = Field(None, alias="clientName")
    good_card: GoodCard | None = Field(None, alias="goodCard")
    last_message: LastMessage | None = Field(None, alias="lastMessage")
