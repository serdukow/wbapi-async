from ..types.pin_feedback_response import PinFeedbackResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class PinFeedback(WbMethod):
    """
    The method allows to pin the feedback to a group of merged product cards or to a product
    card.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/post
    """

    __return__ = PinFeedbackResponse
    __api__ = "feedbacks-api"
    __method__ = "api/feedbacks/v1/pins"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)
