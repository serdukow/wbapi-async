from pydantic import Field

from ..types.stickers_for_assembly_orders_with_delivery_to_pickup_point_item import StickersForAssemblyOrdersWithDeliveryToPickupPointItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetStickersForAssemblyOrdersWithDeliveryToPickupPoint(WbMethod):
    """
    <div class="description_token">Method is available by <a
    href="/openapi/api-information#tag/Authorization/Rules-for-using-API-access-tokens">token
    types</a>:<strong>Personal</strong>,<strong> Service</strong> </div>

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-dbs#tag/DBS-Assembly-Orders/paths/~1api~1marketplace~1v3~1dbs~1orders~1stickers/post
    """

    __return__ = StickersForAssemblyOrdersWithDeliveryToPickupPointItem
    __api__ = "marketplace-api"
    __method__ = "api/marketplace/v3/dbs/orders/stickers"
    __http_method__ = "POST"
    __data_key__ = "stickers"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    type: str = Field(None)
    width: int = Field(None)
    height: int = Field(None)
    orders: list[int] = Field(None)
