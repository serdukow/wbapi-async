from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, UpdateWarehouseResponse


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    warehouse_id: int = Field(alias="warehouseId", exclude=True)
    name: str = Field()
    office_id: int = Field(alias="officeId")
