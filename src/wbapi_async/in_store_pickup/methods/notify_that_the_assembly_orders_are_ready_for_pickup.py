from pydantic import Field

from ...methods.base import WbMethod
from ...types import NotifyThatTheAssemblyOrdersAreReadyForPickupItem, RequestLimit


class NotifyThatTheAssemblyOrdersAreReadyForPickup(WbMethod):
    """
    The method transfers [assembly
    orders](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders)from the `confirm` — on
    assembly—
    [status](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
    tothe `prepare` — ready for pickup — status.

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1prepare/post
    """

    __return__ = NotifyThatTheAssemblyOrdersAreReadyForPickupItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/click-collect/orders/status/prepare"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders_ids: list[int] | None = Field(None, alias="ordersIds")
