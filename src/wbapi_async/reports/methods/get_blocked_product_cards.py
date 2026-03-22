from pydantic import Field

from ...enums import Order2, Sort2
from ...methods.base import WbMethod
from ...types import BlockedProductCardsItem, RequestLimit


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    sort: Sort2 = Field()
    order: Order2 = Field()
