from ...types import AllAssemblyOrdersForReshipmentItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetAllAssemblyOrdersForReshipment(WbMethod):
    """
    Returns all assembly orders that require re-shipment

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1supplies~1orders~1reshipment/get
    """

    __return__ = AllAssemblyOrdersForReshipmentItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/supplies/orders/reshipment"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
