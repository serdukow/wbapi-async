from pydantic import Field

from ..types.number_of_questions_item import NumberOfQuestionsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetNumberOfQuestions(WbMethod):
    """
    The method allows to get the number of questions for requested period

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1questions~1count/get
    """

    __return__ = NumberOfQuestionsItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/questions/count"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)

    date_from: int | None = Field(None, alias="dateFrom")
    date_to: int | None = Field(None, alias="dateTo")
    is_answered: bool | None = Field(True, alias="isAnswered")
