from ...methods.base import WbMethod
from ...types import PinFeedbackResponse, RequestLimit


class PinFeedback(WbMethod):
    """
    The method allows to pin the feedback to a group of merged product cards or to a product card.
    Toget feedback ID, use the [List of pinned and unpinned
    feedback](/openapi/user-communication#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/get)
    method.The method is available for [Jam
    subscription](https://seller.wildberries.ru/monetization/jam)or **Pin a feedback** option in
    the[tariff constructor](https://seller.wildberries.ru/tariff-constructor).

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Pinned-Feedback/paths/~1api~1feedbacks~1v1~1pins/post
    """

    __return__ = PinFeedbackResponse
    __api__ = "feedbacks-api"
    __method__ = "api/feedbacks/v1/pins"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
