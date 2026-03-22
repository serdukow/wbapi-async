from pydantic import Field

from ..types.delete_boxes_from_the_supply_response import DeleteBoxesFromTheSupplyResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class DeleteBoxesFromTheSupply(WbMethod):
    """
    The method deletes boxes from the supply. Available only while the supply is being assembled.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1trbx/delete
    """

    __return__ = DeleteBoxesFromTheSupplyResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/supplies/{supply_id}/trbx"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    supply_id: str = Field(alias="supplyId", exclude=True)
    trbx_ids: list[str] = Field(None, alias="trbxIds")
