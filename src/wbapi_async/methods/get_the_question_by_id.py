from pydantic import Field

from ..types.the_question_by_id_item import TheQuestionByIdItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetTheQuestionById(WbMethod):
    """
    The method allows you to get a question by its ID

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1question/get
    """

    __return__ = TheQuestionByIdItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/question"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)

    id: str = Field(None)
