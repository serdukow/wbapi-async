from ...types import NewOrdersItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetNewOrders(WbMethod):
    """
    Returns a list of all new [orders](/openapi/orders-dbw#tag/DBW-Assembly-Orders).

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1new/get
    """

    __return__ = NewOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbw/orders/new"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
