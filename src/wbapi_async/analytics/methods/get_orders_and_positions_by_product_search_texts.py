from pydantic import Field

from ...finances.enums.period import Period
from ...methods.base import WbMethod
from ...types import OrdersAndPositionsByProductSearchTextsResponse, RequestLimit


class GetOrdersAndPositionsByProductSearchTexts(WbMethod):
    """
    Forms data for a table on the number of orders and positions by queries. The data is specified
    withina period for a specific product.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1product~1orders/post
    """

    __return__ = OrdersAndPositionsByProductSearchTextsResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/search-report/product/orders"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    period: Period = Field()
    nm_id: int = Field(alias="nmId")
    search_texts: list[str] = Field(alias="searchTexts")
