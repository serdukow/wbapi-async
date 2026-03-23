from ...types import RequestLimit
from ...types import UnseenFeedbacksAndQuestionsItem
from ...methods.base import WbMethod


class GetUnseenFeedbacksAndQuestions(WbMethod):
    """
    The method displays information about the seller's unseen feedbacks and questions

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1new-feedbacks-questions/get
    """

    __return__ = UnseenFeedbacksAndQuestionsItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/new-feedbacks-questions"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
