from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, TheFeedbackByIdItem


class GetTheFeedbackById(WbMethod):
    """
    The method allows you to get a feedback by its ID

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedback/get
    """

    __return__ = TheFeedbackByIdItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedback"
    __data_key__ = "data.photoLinks"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    id: str = Field()
