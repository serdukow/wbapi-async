from ..types.new_assembly_orders_item import NewAssemblyOrdersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetNewAssemblyOrders(WbMethod):
    """
    Returns a list of all new [assembly
    orders](/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders/get).

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1new/get
    """

    __return__ = NewAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/orders/new"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)
