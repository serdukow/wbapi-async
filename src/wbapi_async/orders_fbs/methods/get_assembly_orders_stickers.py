from pydantic import Field

from ...methods.base import WbMethod
from ...types import AssemblyOrdersStickersItem, RequestLimit
from ..enums.height import Height
from ..enums.type_ import Type
from ..enums.width import Width


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

    type_: Type = Field(alias="type")
    width: Width = Field()
    height: Height = Field()
    orders: list[int] | None = Field(None)
