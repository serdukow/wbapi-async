from pydantic import Field

from ...methods.base import WbMethod
from ...types import NumberOfFeedbacksItem, RequestLimit


class GetNumberOfFeedbacks(WbMethod):
    """
    The method allows to get the number of feedbacks

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1count/get
    """

    __return__ = NumberOfFeedbacksItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/count"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: int | None = Field(None, alias="dateFrom")
    date_to: int | None = Field(None, alias="dateTo")
    is_answered: bool | None = Field(True, alias="isAnswered")
