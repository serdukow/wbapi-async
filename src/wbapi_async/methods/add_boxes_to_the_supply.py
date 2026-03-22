from pydantic import Field

from ..types.add_boxes_to_the_supply_item import AddBoxesToTheSupplyItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class AddBoxesToTheSupply(WbMethod):
    """
    Adds the required number of boxes to the supply.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1trbx/post
    """

    __return__ = AddBoxesToTheSupplyItem
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/supplies/{supply_id}/trbx"
    __http_method__ = "POST"
    __data_key__ = "trbxIds"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    supply_id: str = Field(alias="supplyId", exclude=True)
    amount: int = Field(None)
