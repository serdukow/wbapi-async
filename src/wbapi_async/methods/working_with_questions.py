from ..types.working_with_questions_item import WorkingWithQuestionsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class WorkingWithQuestions(WbMethod):
    """
    Depending on the request body, you can:

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1questions/patch
    """

    __return__ = WorkingWithQuestionsItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/questions"
    __http_method__ = "PATCH"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)
