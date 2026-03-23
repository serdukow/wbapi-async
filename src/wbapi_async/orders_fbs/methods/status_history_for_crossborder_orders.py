from pydantic import Field

from ...types import RequestLimit
from ...types import StatusHistoryForCrossborderOrdersItem
from ...methods.base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[int] | None = Field(None)
