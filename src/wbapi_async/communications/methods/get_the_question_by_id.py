from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, TheQuestionByIdItem


class GetTheQuestionById(WbMethod):
    """
    The method allows you to get a question by its ID

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1question/get
    """

    __return__ = TheQuestionByIdItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/question"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id_: str = Field(alias="id")
