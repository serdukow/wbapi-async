from pydantic import Field

from ...methods.base import WbMethod
from ...types import PromotionsDetailsItem, RequestLimit


class GetPromotionsDetails(WbMethod):
    """
    Returns detailed information about the selected promotions

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Promotions-Calendar/paths/~1api~1v1~1calendar~1promotions~1details/get
    """

    __return__ = PromotionsDetailsItem
    __api__ = "dp-calendar-api"
    __method__ = "api/v1/calendar/promotions/details"
    __data_key__ = "data.promotions"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    promotion_i_ds: list[int] = Field(alias="promotionIDs")
