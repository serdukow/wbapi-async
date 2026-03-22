from ..types.new_assembly_orders_list_item import NewAssemblyOrdersListItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetNewAssemblyOrdersList(WbMethod):
    """
    The method provides a list of all new [assembly
    orders](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders)that the seller has at the
    timeof the request.

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1v3~1click-collect~1orders~1new/get
    """

    __return__ = NewAssemblyOrdersListItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/click-collect/orders/new"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)
