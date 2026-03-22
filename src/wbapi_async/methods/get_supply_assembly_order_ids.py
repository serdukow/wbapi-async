from pydantic import Field

from ..types.supply_assembly_order_ids_item import SupplyAssemblyOrderIdsItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    supply_id: str = Field(alias="supplyId", exclude=True)
