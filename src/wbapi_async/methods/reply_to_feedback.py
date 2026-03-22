from pydantic import Field

from ..types.reply_to_feedback_response import ReplyToFeedbackResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ReplyToFeedback(WbMethod):
    """
    Allows you to respond to the feedback.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1answer/post
    """

    __return__ = ReplyToFeedbackResponse
    __empty_response__ = True
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/answer"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)

    id: str = Field(None)
    text: str = Field(None)
