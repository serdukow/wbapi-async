from pydantic import Field

from ...methods.base import WbMethod
from ...orders_fbs.enums.height import Height
from ...orders_fbs.enums.type_ import Type
from ...orders_fbs.enums.width import Width
from ...types import OrdersStickersItem, RequestLimit


class GetOrdersStickers(WbMethod):
    """
    Returns a list of stickers for the [assembly
    orders](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1new/get)in
    the
    [statuses](/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1status/post):
    -`confirm` — on assembly - `complete` — on delivery

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbw#tag/DBW-Assembly-Orders/paths/~1api~1v3~1dbw~1orders~1stickers/post
    """

    __return__ = OrdersStickersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/dbw/orders/stickers"
    __http_method__ = "POST"
    __data_key__ = "stickers"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    type_: Type = Field(alias="type")
    width: Width = Field()
    height: Height = Field()
    orders: list[int] | None = Field(None)
