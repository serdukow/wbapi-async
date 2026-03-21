from pydantic import Field

from ..types.delete_warehouse_response import DeleteWarehouseResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class DeleteWarehouse(WbMethod):
    """
    Deletes the seller's warehouse.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses~1%7BwarehouseId%7D/delete
    """

    __return__ = DeleteWarehouseResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/warehouses/{warehouse_id}"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    warehouse_id: int = Field(alias="warehouseId", exclude=True)
