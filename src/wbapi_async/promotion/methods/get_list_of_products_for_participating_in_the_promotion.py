from pydantic import Field

from ...types import ListOfProductsForParticipatingInThePromotionItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetListOfProductsForParticipatingInThePromotion(WbMethod):
    """
    Returns a list of products suitable for participation in the promotion.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Promotions-Calendar/paths/~1api~1v1~1calendar~1promotions~1nomenclatures/get
    """

    __return__ = ListOfProductsForParticipatingInThePromotionItem
    __api__ = "dp-calendar-api"
    __method__ = "api/v1/calendar/promotions/nomenclatures"
    __data_key__ = "data.nomenclatures"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    promotion_id: int = Field(alias="promotionID")
    in_action: bool = Field(False, alias="inAction")
    limit: int | None = Field(None)
    offset: int | None = Field(None)
