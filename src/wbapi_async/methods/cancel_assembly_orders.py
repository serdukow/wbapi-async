from pydantic import Field

from ..types.cancel_assembly_orders_item import CancelAssemblyOrdersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CancelAssemblyOrders(WbMethod):
    """
    The method transfers [assembly orders](/openapi/orders-dbs#tag/DBS-Assembly-Orders) with the
    [statuses](/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1info/post)
    `new`,`confirm` и `deliver` to the status `cancel` — canceled by the supplier.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1status~1cancel/post
    """

    __return__ = CancelAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/status/cancel"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=10)

    orders_ids: list[int] | None = Field(None, alias="ordersIds")
