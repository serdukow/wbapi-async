from pydantic import Field

from ...types import MoveTheSupplyToTheDeliveryResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    supply_id: str = Field(alias="supplyId", exclude=True)
