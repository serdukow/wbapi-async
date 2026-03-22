from pydantic import Field

from ...methods.base import WbMethod
from ...types import ReplyToFeedbackResponse, RequestLimit


class ReplyToFeedback(WbMethod):
    """
    Allows you to respond to the feedback. There is no validation by `feedback ID`: if an incorrect
    valueis provided in the request, you will not receive an error.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1answer/post
    """

    __return__ = ReplyToFeedbackResponse
    __empty_response__ = True
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/answer"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id: str = Field()
    text: str = Field()
