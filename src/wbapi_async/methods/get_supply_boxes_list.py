from pydantic import Field

from ..types.supply_boxes_list_item import SupplyBoxesListItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetSupplyBoxesList(WbMethod):
    """
    Returns supply boxes list.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbs#tag/FBS-Supplies/paths/~1api~1v3~1supplies~1%7BsupplyId%7D~1trbx/get
    """

    __return__ = SupplyBoxesListItem
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/supplies/{supply_id}/trbx"
    __data_key__ = "trbxes"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    supply_id: str = Field(alias="supplyId", exclude=True)
