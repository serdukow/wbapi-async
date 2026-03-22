from pydantic import Field

from ..types.supply_products_response import SupplyProductsResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetSupplyProducts(WbMethod):
    """
    The method returns information about the products in the supply.

    Source: https://dev.wildberries.ru/en/docs/openapi/orders-fbw#tag/Supplies-Information/paths/~1api~1v1~1supplies~1%7BID%7D~1goods/get
    """

    __return__ = SupplyProductsResponse
    __api__ = "supplies-api"
    __method__ = ""
    __method_template__ = "api/v1/supplies/{id}/goods"

    request_limit: RequestLimit = RequestLimit(period=60, limit=30, interval=2, burst=10)

    limit: int | None = Field(100)
    offset: int | None = Field(0)
    is_preorder_id: bool | None = Field(False, alias="isPreorderID")
    id: int = Field(alias="ID", exclude=True)
