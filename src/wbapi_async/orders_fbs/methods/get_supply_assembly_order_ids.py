from pydantic import Field

from ...types import RequestLimit
from ...types import SupplyAssemblyOrderIdsItem
from ...methods.base import WbMethod


class GetSupplyAssemblyOrderIds(WbMethod):
    """
    The method returns assembly orders IDs assigned to the supply.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1marketplace~1v3~1supplies~1%7BsupplyId%7D~1order-ids/get
    """

    __return__ = SupplyAssemblyOrderIdsItem
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/marketplace/v3/supplies/{supply_id}/order-ids"
    __data_key__ = "orderIds"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    supply_id: str = Field(alias="supplyId", exclude=True)
