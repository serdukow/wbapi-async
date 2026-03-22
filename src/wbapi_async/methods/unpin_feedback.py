from ..types.unpin_feedback_response import UnpinFeedbackResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class UnpinFeedback(WbMethod):
    """
    The method allows to unpin the feedback in a group of merged product cards or a product
    card.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/delete
    """

    __return__ = UnpinFeedbackResponse
    __api__ = "feedbacks-api"
    __method__ = "api/feedbacks/v1/pins"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)
