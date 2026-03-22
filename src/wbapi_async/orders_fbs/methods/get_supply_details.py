from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, SupplyDetailsResponse


class GetSupplyDetails(WbMethod):
    """
    Returns supply details.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D/get
    """

    __return__ = SupplyDetailsResponse
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/supplies/{supply_id}"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    supply_id: str = Field(alias="supplyId", exclude=True)
