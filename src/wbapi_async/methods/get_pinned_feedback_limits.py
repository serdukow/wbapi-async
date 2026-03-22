from ..types.pinned_feedback_limits_response import PinnedFeedbackLimitsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetPinnedFeedbackLimits(WbMethod):
    """
    The method returns the pinned feedback limits for a tariff and subscription.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins~1limits/get
    """

    __return__ = PinnedFeedbackLimitsResponse
    __api__ = "feedbacks-api"
    __method__ = "api/feedbacks/v1/pins/limits"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)
