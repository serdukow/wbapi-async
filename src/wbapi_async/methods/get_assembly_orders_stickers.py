from pydantic import Field

from ..types.assembly_orders_stickers_item import AssemblyOrdersStickersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetAssemblyOrdersStickers(WbMethod):
    """
    Returns a list of stickers according to the requested assembly orders.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1stickers/post
    """

    __return__ = AssemblyOrdersStickersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/orders/stickers"
    __http_method__ = "POST"
    __data_key__ = "stickers"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    type: str = Field(None)
    width: int = Field(None)
    height: int = Field(None)
    orders: list[int] | None = Field(None)
