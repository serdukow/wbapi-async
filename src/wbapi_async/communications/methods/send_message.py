from ...methods.base import WbMethod
from ...types import RequestLimit, SendMessageItem


class SendMessage(WbMethod):
    """
    Sends message to the buyer.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Chat/paths/~1api~1v1~1seller~1message/post
    """

    __return__ = SendMessageItem
    __api__ = "buyer-chat-api"
    __method__ = "api/v1/seller/message"
    __http_method__ = "POST"
    __data_key__ = "errors"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
