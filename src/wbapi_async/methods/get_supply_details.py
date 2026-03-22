from pydantic import Field

from ..types.supply_details_response import SupplyDetailsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetSupplyDetails(WbMethod):
    """
    The method returns supply details by ID.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Supplies-Information/paths/~1api~1v1~1supplies~1%7BID%7D/get
    """

    __return__ = SupplyDetailsResponse
    __api__ = "supplies-api"
    __method__ = ""
    __method_template__ = "api/v1/supplies/{id}"

    request_limit: RequestLimit = RequestLimit(period=60, limit=30, interval=2, burst=10)

    id: int = Field(alias="ID", exclude=True)
    is_preorder_id: bool | None = Field(False, alias="isPreorderID")
