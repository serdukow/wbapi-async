from pydantic import Field

from ..types.return_product_by_feedback_id_item import ReturnProductByFeedbackIdItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ReturnProductByFeedbackId(WbMethod):
    """
    The method allows requesting a return for a product for which a feedback has been left.

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1order~1return/post
    """

    __return__ = ReturnProductByFeedbackIdItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/order/return"
    __http_method__ = "POST"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)

    feedback_id: str | None = Field(None, alias="feedbackId")
