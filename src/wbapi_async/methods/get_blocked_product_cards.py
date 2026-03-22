from pydantic import Field

from ..types.blocked_product_cards_item import BlockedProductCardsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetBlockedProductCards(WbMethod):
    """
    Returns the list of [blocked product
    cards](https://seller.wildberries.ru/analytics-reports/banned-products)

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Hidden-Products/paths/~1api~1v1~1analytics~1banned-products~1blocked/get
    """

    __return__ = BlockedProductCardsItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/banned-products/blocked"
    __data_key__ = "report"

    request_limit: RequestLimit = RequestLimit(period=10, limit=1, interval=10, burst=6)

    sort: str = Field(None)
    order: str = Field(None)
