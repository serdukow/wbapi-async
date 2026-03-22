from pydantic import Field

from ..types.move_the_supply_to_the_delivery_response import MoveTheSupplyToTheDeliveryResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class MoveTheSupplyToTheDelivery(WbMethod):
    """
    Closes the supply and moves all assembly orders to `complete` (`In Delivery`) status. You
    cannotadd any assembly orders to the supply after it is closed.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1deliver/patch
    """

    __return__ = MoveTheSupplyToTheDeliveryResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/supplies/{supply_id}/deliver"
    __http_method__ = "PATCH"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    supply_id: str = Field(alias="supplyId", exclude=True)
