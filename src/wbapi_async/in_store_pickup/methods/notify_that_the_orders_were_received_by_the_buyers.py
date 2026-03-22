from pydantic import Field

from ...methods.base import WbMethod
from ...types import NotifyThatTheOrdersWereReceivedByTheBuyersItem, RequestLimit


class NotifyThatTheOrdersWereReceivedByTheBuyers(WbMethod):
    """
    The method transfers [assembly
    orders](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders)from the `prepare` — ready
    forpickup —
    [status](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
    tothe `receive` — received by the buyer — status.

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1receive/post
    """

    __return__ = NotifyThatTheOrdersWereReceivedByTheBuyersItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/click-collect/orders/status/receive"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders_ids: list[int] | None = Field(None, alias="ordersIds")
