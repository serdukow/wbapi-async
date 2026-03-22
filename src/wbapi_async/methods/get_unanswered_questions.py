from ..types.unanswered_questions_item import UnansweredQuestionsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetUnansweredQuestions(WbMethod):
    """
    The method allows you to get the number of unanswered questions for today and for all time

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1questions~1count-unanswered/get
    """

    __return__ = UnansweredQuestionsItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/questions/count-unanswered"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)
