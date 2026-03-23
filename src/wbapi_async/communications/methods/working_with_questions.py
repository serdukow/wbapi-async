from ...types import RequestLimit
from ...types import WorkingWithQuestionsItem
from ...methods.base import WbMethod


class WorkingWithQuestions(WbMethod):
    """
    Depending on the request body, you can: - View question. - Reject question. - Answer question
    oredit the answer.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Questions/paths/~1api~1v1~1questions/patch
    """

    __return__ = WorkingWithQuestionsItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/questions"
    __http_method__ = "PATCH"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
