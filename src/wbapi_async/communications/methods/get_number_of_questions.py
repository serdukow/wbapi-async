from pydantic import Field

from ...types import NumberOfQuestionsItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetNumberOfQuestions(WbMethod):
    """
    The method allows to get the number of questions for requested period

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1questions~1count/get
    """

    __return__ = NumberOfQuestionsItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/questions/count"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: int | None = Field(None, alias="dateFrom")
    date_to: int | None = Field(None, alias="dateTo")
    is_answered: bool | None = Field(True, alias="isAnswered")
