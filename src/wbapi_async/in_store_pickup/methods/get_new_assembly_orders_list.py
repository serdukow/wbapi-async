from ...methods.base import WbMethod
from ...types import NewAssemblyOrdersListItem, RequestLimit


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
