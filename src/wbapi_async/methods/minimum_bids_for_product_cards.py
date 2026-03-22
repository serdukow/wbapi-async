from pydantic import Field

from ..types.minimum_bids_for_product_cards_item import MinimumBidsForProductCardsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=20, interval=3, burst=5)

    advert_id: int = Field(None)
    nm_ids: list[int] = Field(None)
    payment_type: str = Field(None)
    placement_types: list[str] = Field(None)
