from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, StickersForCrossborderAssemblyOrdersItem


class GetStickersForCrossborderAssemblyOrders(WbMethod):
    """
    Returns a list of stickers for cross-border assembly orders in PDF.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1stickers~1cross-border/post
    """

    __return__ = StickersForCrossborderAssemblyOrdersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/orders/stickers/cross-border"
    __http_method__ = "POST"
    __data_key__ = "stickers"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    orders: list[int] | None = Field(None, alias="orders")
