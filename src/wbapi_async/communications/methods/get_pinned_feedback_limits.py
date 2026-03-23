from ...types import PinnedFeedbackLimitsResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetPinnedFeedbackLimits(WbMethod):
    """
    The method returns the pinned feedback limits for a tariff and subscription.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins~1limits/get
    """

    __return__ = PinnedFeedbackLimitsResponse
    __api__ = "feedbacks-api"
    __method__ = "api/feedbacks/v1/pins/limits"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
