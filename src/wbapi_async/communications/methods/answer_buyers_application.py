from pydantic import Field

from ...methods.base import WbMethod
from ...types import AnswerBuyersApplicationResponse, RequestLimit


class AnswerBuyersApplication(WbMethod):
    """
    Sends an answer to the buyers application for product return.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Buyers-Returns/paths/~1api~1v1~1claim/patch
    """

    __return__ = AnswerBuyersApplicationResponse
    __empty_response__ = True
    __api__ = "returns-api"
    __method__ = "api/v1/claim"
    __http_method__ = "PATCH"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id_: str = Field(alias="id")
    action: str = Field()
    comment: str | None = Field(None)
