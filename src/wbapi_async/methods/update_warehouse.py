from pydantic import Field

from ..types.update_warehouse_response import UpdateWarehouseResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class UpdateWarehouse(WbMethod):
    """
    Updates the seller's warehouse details. Changing the linked office is allowed once per day. You
    cannotlink an office that is already in use.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses~1%7BwarehouseId%7D/put
    """

    __return__ = UpdateWarehouseResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/warehouses/{warehouse_id}"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    warehouse_id: int = Field(alias="warehouseId", exclude=True)
    name: str = Field(None)
    office_id: int = Field(None, alias="officeId")
