from pydantic import Field

from ...types import AssemblyOrderStatusesItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetAssemblyOrderStatuses(WbMethod):
    """
    Returns the statuses of [assembly orders](/openapi/orders-dbs#tag/DBS-Assembly-Orders) based on
    thelist of assembly order IDs.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post
    """

    __return__ = AssemblyOrderStatusesItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/status/info"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders_ids: list[int] | None = Field(None, alias="ordersIds")
