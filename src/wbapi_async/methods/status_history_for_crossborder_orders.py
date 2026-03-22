from pydantic import Field

from ..types.status_history_for_crossborder_orders_item import StatusHistoryForCrossborderOrdersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class StatusHistoryForCrossborderOrders(WbMethod):
    """
    Returns status history for cross-border orders

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1status~1history/post
    """

    __return__ = StatusHistoryForCrossborderOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/orders/status/history"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    orders: list[int] | None = Field(None)
