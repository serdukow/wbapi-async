from pydantic import Field

from ..types.number_of_feedbacks_item import NumberOfFeedbacksItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetNumberOfFeedbacks(WbMethod):
    """
    The method allows to get the number of feedbacks

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1count/get
    """

    __return__ = NumberOfFeedbacksItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/count"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)

    date_from: int | None = Field(None, alias="dateFrom")
    date_to: int | None = Field(None, alias="dateTo")
    is_answered: bool | None = Field(True, alias="isAnswered")
