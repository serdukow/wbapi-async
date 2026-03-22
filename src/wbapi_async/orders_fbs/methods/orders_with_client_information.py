from pydantic import Field

from ...methods.base import WbMethod
from ...types import OrdersWithClientInformationItem, RequestLimit


class OrdersWithClientInformation(WbMethod):
    """
    The method allows getting information about the client by assembly order ID. Only for
    cross-borderorders from **Turkey**

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1client/post
    """

    __return__ = OrdersWithClientInformationItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/orders/client"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[int] | None = Field(None)
