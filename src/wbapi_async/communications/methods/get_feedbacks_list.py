from pydantic import Field

from ...enums import Order
from ...types import FeedbacksListItem
from ...types import RequestLimit
from ...methods.base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    is_answered: bool = Field(alias="isAnswered")
    nm_id: int | None = Field(None, alias="nmId")
    take: int = Field()
    skip: int = Field()
    order: Order | None = Field(None)
    date_from: int | None = Field(None, alias="dateFrom")
    date_to: int | None = Field(None, alias="dateTo")
