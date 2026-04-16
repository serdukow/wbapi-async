from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, StickersForAssemblyOrdersWithDeliveryToPickupPointItem


class GetStickersForAssemblyOrdersWithDeliveryToPickupPoint(WbMethod):
    """
    Method is available by token types : Personal , Service

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1stickers/post
    """

    __return__ = StickersForAssemblyOrdersWithDeliveryToPickupPointItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/stickers"
    __http_method__ = "POST"
    __data_key__ = "stickers"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    type_: str = Field(alias="type")
    width: int = Field(alias="width")
    height: int = Field(alias="height")
    orders: list[int] = Field(alias="orders")
