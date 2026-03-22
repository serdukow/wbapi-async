from pydantic import Field

from ...enums import PaymentType
from ...methods.base import WbMethod
from ...types import MinimumBidsForProductCardsItem, RequestLimit


class MinimumBidsForProductCards(WbMethod):
    """
    Method allows minimum bids for product cards in kopecks depending on the payment type and
    placements.

    Source: https://dev.wildberries.ru/en/docs/openapi/promotion#tag/Campaigns-Creation/paths/~1api~1advert~1v1~1bids~1min/post
    """

    __return__ = MinimumBidsForProductCardsItem
    __api__ = "advert-api"
    __method__ = "api/advert/v1/bids/min"
    __http_method__ = "POST"
    __data_key__ = "bids"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    advert_id: int = Field()
    nm_ids: list[int] = Field()
    payment_type: PaymentType = Field()
    placement_types: list[str] = Field()
