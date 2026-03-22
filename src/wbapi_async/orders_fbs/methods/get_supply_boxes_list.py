from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, SupplyBoxesListItem


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    supply_id: str = Field(alias="supplyId", exclude=True)
