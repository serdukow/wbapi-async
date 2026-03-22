from pydantic import Field

from ..types.answer_buyers_application_response import AnswerBuyersApplicationResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=20, interval=3, burst=10)

    id: str = Field(None)
    action: str = Field(None)
    comment: str | None = Field(None)
