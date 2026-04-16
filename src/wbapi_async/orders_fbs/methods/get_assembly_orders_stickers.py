from pydantic import Field

from ...methods.base import WbMethod
from ...types import AssemblyOrdersStickersItem, RequestLimit


class GetAssemblyOrdersStickers(WbMethod):
    """
    Returns a list of stickers according to the requested assembly orders. You can request a
    stickerin `svg`, `zplv` (vertical), `zplh` (horizontal) and `png` formats.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Assembly-Orders/paths/~1api~1v3~1orders~1stickers/post
    """

    __return__ = AssemblyOrdersStickersItem
    __api__ = "marketplace-api"
    __method__ = "api/v3/orders/stickers"
    __http_method__ = "POST"
    __data_key__ = "stickers"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    type_: str = Field(alias="type")
    width: int = Field(alias="width")
    height: int = Field(alias="height")
    orders: list[int] | None = Field(None, alias="orders")
