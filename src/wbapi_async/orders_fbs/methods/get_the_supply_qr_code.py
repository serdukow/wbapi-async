from pydantic import Field

from ...enums import Type
from ...methods.base import WbMethod
from ...types import RequestLimit, TheSupplyQrCodeResponse


class GetTheSupplyQrCode(WbMethod):
    """
    Returns the QR code in svg, zplv (vertical), zplh (horizontal), png. Available only after the
    supplyhas been transferred to the delivery. Available dimensions: 580x400 px

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1barcode/get
    """

    __return__ = TheSupplyQrCodeResponse
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/supplies/{supply_id}/barcode"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    supply_id: str = Field(alias="supplyId", exclude=True)
    type: Type = Field()
