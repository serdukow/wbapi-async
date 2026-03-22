from pydantic import Field

from ..types.assembly_order_statuses_item import AssemblyOrderStatusesItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetAssemblyOrderStatuses(WbMethod):
    """
    This method is deprecated. It will be removed on [May
    19](https://dev.wildberries.ru/en/release-notes?id=474)

    Source: https://dev.wildberries.ru/en/docs/openapi/in-store-pickup#tag/In-Store-Pickup-Assembly-Orders/paths/~1api~1v3~1click-collect~1orders~1status/post
    """

    __return__ = AssemblyOrderStatusesItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/click-collect/orders/status"
    __http_method__ = "POST"
    __data_key__ = "orders"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[int] | None = Field(None)
