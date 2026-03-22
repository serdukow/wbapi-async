from ..types.unanswered_feedbacks_item import UnansweredFeedbacksItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetUnansweredFeedbacks(WbMethod):
    """
    The method allows you to get the number of unanswered feedbacks for today, for all time.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1count-unanswered/get
    """

    __return__ = UnansweredFeedbacksItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/count-unanswered"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)
