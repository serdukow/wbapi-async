from ...methods.base import WbMethod
from ...types import RequestLimit, UnpinFeedbackResponse


class UnpinFeedback(WbMethod):
    """
    The method allows to unpin the feedback in a group of merged product cards or a product card.
    Toget `pinId` — feedback pinning operation ID, use the [List of pinned and unpinned
    feedback](/openapi/user-communication#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/get)
    method.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/delete
    """

    __return__ = UnpinFeedbackResponse
    __api__ = "feedbacks-api"
    __method__ = "api/feedbacks/v1/pins"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
