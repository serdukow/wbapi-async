from pydantic import Field

from ...methods.base import WbMethod
from ...types import DeleteBoxesFromTheSupplyResponse, RequestLimit


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    supply_id: str = Field(alias="supplyId", exclude=True)
    trbx_ids: list[str] = Field(alias="trbxIds")
