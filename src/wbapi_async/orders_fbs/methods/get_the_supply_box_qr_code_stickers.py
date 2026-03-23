from pydantic import Field

from ...enums import Type
from ...methods.base import WbMethod
from ...types import RequestLimit, TheSupplyBoxQrCodeStickersItem


class GetTheSupplyBoxQrCodeStickers(WbMethod):
    """
    Returns QR-code stickers in svg, zplv (vertical), zplh (horizontal), png. Available only if
    thereare assembly orders in the box. Stickers dimensions: 580x400 px.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1trbx~1stickers/post
    """

    __return__ = TheSupplyBoxQrCodeStickersItem
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/supplies/{supply_id}/trbx/stickers"
    __http_method__ = "POST"
    __data_key__ = "stickers"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    supply_id: str = Field(alias="supplyId", exclude=True)
    type_: Type = Field(alias="type")
    trbx_ids: list[str] = Field(alias="trbxIds")
