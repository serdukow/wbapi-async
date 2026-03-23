from pydantic import Field

from ...types import ChatEventsItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetChatEvents(WbMethod):
    """
    Returns an event list for all chats.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Chat/paths/~1api~1v1~1seller~1events/get
    """

    __return__ = ChatEventsItem
    __api__ = "buyer-chat-api"
    __method__ = "api/v1/seller/events"
    __data_key__ = "result.events"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    next: int | None = Field(None)
