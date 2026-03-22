from ...methods.base import WbMethod
from ...types import ChatListItem, RequestLimit


class GetChatList(WbMethod):
    """
    Returns a list of all seller's chats.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Chat/paths/~1api~1v1~1seller~1chats/get
    """

    __return__ = ChatListItem
    __api__ = "buyer-chat-api"
    __method__ = "api/v1/seller/chats"
    __data_key__ = "result"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
