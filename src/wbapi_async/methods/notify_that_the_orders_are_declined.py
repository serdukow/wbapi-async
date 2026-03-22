from pydantic import Field

from ..types.notify_that_the_orders_are_declined_item import NotifyThatTheOrdersAreDeclinedItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class NotifyThatTheOrdersAreDeclined(WbMethod):
    """
    The method transfers [assembly
    orders](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders)from the `prepare` — ready
    forpickup —
    [status](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
    tothe `reject` — refusal upon receipt — status.

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1reject/post
    """

    __return__ = NotifyThatTheOrdersAreDeclinedItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/click-collect/orders/status/reject"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=10)

    orders_ids: list[int] | None = Field(None, alias="ordersIds")
