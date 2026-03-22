from pydantic import Field

from ..types.file_from_the_message_response import FileFromTheMessageResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetFileFromTheMessage(WbMethod):
    """
    The method provides a file or image from the message by its ID.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Chat/paths/~1api~1v1~1seller~1download~1%7Bid%7D/get
    """

    __return__ = FileFromTheMessageResponse
    __empty_response__ = True
    __api__ = "buyer-chat-api"
    __method__ = ""
    __method_template__ = "api/v1/seller/download/{id}"

    request_limit: RequestLimit = RequestLimit(period=10, limit=10, interval=1, burst=10)

    id: str = Field(exclude=True)
