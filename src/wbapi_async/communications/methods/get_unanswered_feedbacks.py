from ...types import RequestLimit
from ...types import UnansweredFeedbacksItem
from ...methods.base import WbMethod


class GetUnansweredFeedbacks(WbMethod):
    """
    The method allows you to get the number of unanswered feedbacks for today, for all time.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1count-unanswered/get
    """

    __return__ = UnansweredFeedbacksItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/count-unanswered"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
