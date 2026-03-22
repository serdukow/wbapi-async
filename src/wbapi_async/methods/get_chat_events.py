from pydantic import Field

from ..types.chat_events_item import ChatEventsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetChatEvents(WbMethod):
    """
    Returns an event list for all chats.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Chat/paths/~1api~1v1~1seller~1events/get
    """

    __return__ = ChatEventsItem
    __api__ = "buyer-chat-api"
    __method__ = "api/v1/seller/events"
    __data_key__ = "result.events"

    request_limit: RequestLimit = RequestLimit(period=10, limit=10, interval=1, burst=10)

    next: int | None = Field(None)
