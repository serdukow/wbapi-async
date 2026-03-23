from pydantic import Field

from ...methods.base import WbMethod
from ...types import FileFromTheMessageResponse, RequestLimit


class GetFileFromTheMessage(WbMethod):
    """
    The method provides a file or image from the message by its ID.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Chat/paths/~1api~1v1~1seller~1download~1%7Bid%7D/get
    """

    __return__ = FileFromTheMessageResponse
    __empty_response__ = True
    __api__ = "buyer-chat-api"
    __method__ = ""
    __method_template__ = "api/v1/seller/download/{id_}"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id_: str = Field(alias="id", exclude=True)
