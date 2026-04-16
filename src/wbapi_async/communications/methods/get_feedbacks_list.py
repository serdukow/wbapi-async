from pydantic import Field

from ...methods.base import WbMethod
from ...types import FeedbacksListItem, RequestLimit


class GetFeedbacksList(WbMethod):
    """
    The method allows you to get a list of feedbacks by the specified parameters with pagination
    andsorting

    Source: https://dev.wildberries.ru/en/docs/openapi/communications#tag/Feedbacks/paths/~1api~1v1~1feedbacks/get
    """

    __return__ = FeedbacksListItem
    __api__ = "feedbacks-api"
    __method__ = "api/v1/feedbacks"
    __data_key__ = "data.feedbacks"
    __pagination__ = "take_skip"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    is_answered: bool = Field(alias="isAnswered")
    nm_id: int | None = Field(None, alias="nmId")
    take: int = Field(alias="take")
    skip: int = Field(alias="skip")
    order: str | None = Field(None, alias="order")
    date_from: int | None = Field(None, alias="dateFrom")
    date_to: int | None = Field(None, alias="dateTo")
