from pydantic import Field

from ..types.cancel_the_assembly_orders_item import CancelTheAssemblyOrdersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CancelTheAssemblyOrders(WbMethod):
    """
    The method transfers [assembly
    orders](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders)from the `new`, `confirm`,
    `prepare`
    [statuses](/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1info/post)
    tothe `cancel` — canceled by the seller — status.

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1marketplace~1v3~1click-collect~1orders~1status~1cancel/post
    """

    __return__ = CancelTheAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/click-collect/orders/status/cancel"
    __http_method__ = "POST"
    __data_key__ = "results"

    request_limit: RequestLimit = RequestLimit(period=1, limit=1, interval=1, burst=10)

    orders_ids: list[int] | None = Field(None, alias="ordersIds")
