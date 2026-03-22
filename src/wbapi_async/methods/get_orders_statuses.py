from pydantic import Field

from ..types.orders_statuses_item import OrdersStatusesItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetOrdersStatuses(WbMethod):
    """
    This method is deprecated. It will be removed on [April
    13](https://dev.wildberries.ru/en/release-notes?id=378)

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1orders~1status/post
    """

    __return__ = OrdersStatusesItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbs/orders/status"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[int] = Field(None)
