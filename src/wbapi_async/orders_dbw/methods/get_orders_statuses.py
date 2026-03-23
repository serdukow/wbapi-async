from pydantic import Field

from ...types import OrdersStatusesItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetOrdersStatuses(WbMethod):
    """
    Returns the statuses of orders based on the provided list of assembly order IDs

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1status/post
    """

    __return__ = OrdersStatusesItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbw/orders/status"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[int] = Field()
