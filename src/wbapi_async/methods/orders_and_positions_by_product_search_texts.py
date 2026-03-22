from typing import Any

from pydantic import Field

from ..types.orders_and_positions_by_product_search_texts_response import OrdersAndPositionsByProductSearchTextsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class OrdersAndPositionsByProductSearchTexts(WbMethod):
    """
    Forms data for a table on the number of orders and positions by queries. The data is specified
    withina period for a specific product.<br><br>

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Search-Queries-for-Your-Items/paths/~1api~1v2~1search-report~1product~1orders/post
    """

    __return__ = OrdersAndPositionsByProductSearchTextsResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/search-report/product/orders"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)

    period: dict[str, Any] = Field(None)
    nm_id: int = Field(None, alias="nmId")
    search_texts: list[str] = Field(None, alias="searchTexts")
