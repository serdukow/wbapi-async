from pydantic import Field

from ..types.delete_the_supply_response import DeleteTheSupplyResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class DeleteTheSupply(WbMethod):
    """
    Deleted the supply if it is active and does not contain any assembly orders.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D/delete
    """

    __return__ = DeleteTheSupplyResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/supplies/{supply_id}"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    supply_id: str = Field(alias="supplyId", exclude=True)
