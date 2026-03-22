from pydantic import Field

from ..types.stickers_for_crossborder_assembly_orders_item import StickersForCrossborderAssemblyOrdersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetStickersForCrossborderAssemblyOrders(WbMethod):
    """
    Returns a list of stickers for cross-border assembly orders in PDF.<br><br>

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1stickers~1cross-border/post
    """

    __return__ = StickersForCrossborderAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/orders/stickers/cross-border"
    __http_method__ = "POST"
    __data_key__ = "stickers"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    orders: list[int] | None = Field(None)
