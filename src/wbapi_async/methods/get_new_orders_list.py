from ..types.new_orders_list_item import NewOrdersListItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetNewOrdersList(WbMethod):
    """
    Returns a list of all new orders for the seller at the moment

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1v3~1dbs~1orders~1new/get
    """

    __return__ = NewOrdersListItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbs/orders/new"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)
