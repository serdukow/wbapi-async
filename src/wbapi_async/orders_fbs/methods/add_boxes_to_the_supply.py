from pydantic import Field

from ...types import AddBoxesToTheSupplyItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class AddBoxesToTheSupply(WbMethod):
    """
    Adds the required number of boxes to the supply. You should add boxes only to supplies shipped
    tothe pickup points. You can add boxes to an open supply only. You can add as many boxes as
    thereare items in the supply, plus one more box.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1trbx/post
    """

    __return__ = AddBoxesToTheSupplyItem
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/supplies/{supply_id}/trbx"
    __http_method__ = "POST"
    __data_key__ = "trbxIds"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    supply_id: str = Field(alias="supplyId", exclude=True)
    amount: int = Field()
