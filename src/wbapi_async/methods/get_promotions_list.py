from pydantic import Field

from ..types.promotions_list_item import PromotionsListItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetPromotionsList(WbMethod):
    """
    Returns a promotions list with dates and times of occurrence

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Promotions-Calendar/paths/~1api~1v1~1calendar~1promotions/get
    """

    __return__ = PromotionsListItem
    __api__ = "dp-calendar-api"
    __method__ = "api/v1/calendar/promotions"
    __data_key__ = "data.promotions"

    request_limit: RequestLimit = RequestLimit(period=6, limit=10, interval=600, burst=5)

    start_date_time: str = Field(None, alias="startDateTime")
    end_date_time: str = Field(None, alias="endDateTime")
    all_promo: bool = Field(False, alias="allPromo")
    limit: int | None = Field(None)
    offset: int | None = Field(None)
