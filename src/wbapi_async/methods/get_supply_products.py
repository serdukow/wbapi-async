from pydantic import Field

from ..types.request_limit import RequestLimit
from ..types.supply_product import SupplyProduct
from .base import WbMethod


class GetSupplyProducts(WbMethod):
    """
    Returns information about the products in a supply.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Supplies-Information/paths/~1api~1v1~1supplies~1%7BID%7D~1goods/get
    """

    __return__ = SupplyProduct
    __api__ = "supplies-api"
    __method__ = ""
    __method_template__ = "api/v1/supplies/{supply_id}/goods"

    request_limit: RequestLimit = RequestLimit(period=60, limit=30, interval=2000, burst=10)

    supply_id: int = Field(exclude=True)
    limit: int | None = Field(100, alias="limit")
    offset: int = Field(0, alias="offset")
    is_preorder_id: bool | None = Field(None, alias="isPreorderID")
