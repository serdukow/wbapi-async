from pydantic import Field

from ..types.the_feedback_by_id_item import TheFeedbackByIdItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetTheFeedbackById(WbMethod):
    """
    The method allows you to get a feedback by its ID

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedback/get
    """

    __return__ = TheFeedbackByIdItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedback"
    __data_key__ = "data.photoLinks"

    request_limit: RequestLimit = RequestLimit(period=1, limit=3, interval=333, burst=6)

    id: str = Field(None)
