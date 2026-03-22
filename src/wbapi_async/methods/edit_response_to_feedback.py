from pydantic import Field

from ..types.edit_response_to_feedback_response import EditResponseToFeedbackResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class EditResponseToFeedback(WbMethod):
    """
    Allows you to edit an already sent response to the feedback.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1answer/patch
    """

    __return__ = EditResponseToFeedbackResponse
    __empty_response__ = True
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/answer"
    __http_method__ = "PATCH"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)

    id: str = Field(None)
    text: str = Field(None)
