from pydantic import Field

from ..types.the_supply_box_qr_code_stickers_item import TheSupplyBoxQrCodeStickersItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetTheSupplyBoxQrCodeStickers(WbMethod):
    """
    Returns QR-code stickers in svg, zplv (vertical), zplh (horizontal), png.<br>

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1trbx~1stickers/post
    """

    __return__ = TheSupplyBoxQrCodeStickersItem
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/supplies/{supply_id}/trbx/stickers"
    __http_method__ = "POST"
    __data_key__ = "stickers"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    supply_id: str = Field(alias="supplyId", exclude=True)
    type: str = Field(None)
    trbx_ids: list[str] = Field(None, alias="trbxIds")
