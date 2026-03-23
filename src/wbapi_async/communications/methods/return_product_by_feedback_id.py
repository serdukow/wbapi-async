from pydantic import Field

from ...types import RequestLimit
from ...types import ReturnProductByFeedbackIdItem
from ...methods.base import WbMethod


class ReturnProductByFeedbackId(WbMethod):
    """
    The method allows requesting a return for a product for which a feedback has been left. Return
    isavailable for feedbacks with `"isAbleReturnProductOrders": true`

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks~1order~1return/post
    """

    __return__ = ReturnProductByFeedbackIdItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks/order/return"
    __http_method__ = "POST"
    __data_key__ = "additionalErrors"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    feedback_id: str | None = Field(None, alias="feedbackId")
