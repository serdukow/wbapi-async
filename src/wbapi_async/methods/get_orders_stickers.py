from pydantic import Field

from ..types.orders_stickers_item import OrdersStickersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetOrdersStickers(WbMethod):
    """
    Returns a list of stickers for the [assembly
    orders](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1new/get)in
    the
    [statuses](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1status/post):

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1stickers/post
    """

    __return__ = OrdersStickersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbw/orders/stickers"
    __http_method__ = "POST"
    __data_key__ = "stickers"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    type: str = Field(None)
    width: int = Field(None)
    height: int = Field(None)
    orders: list[int] | None = Field(None)
