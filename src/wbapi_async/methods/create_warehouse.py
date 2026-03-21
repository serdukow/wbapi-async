from pydantic import Field

from ..types.create_warehouse_response import CreateWarehouseResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CreateWarehouse(WbMethod):
    """
    Create Warehouse

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses/paths/~1api~1v3~1warehouses/post
    """

    __return__ = CreateWarehouseResponse
    __api__ = "marketplace-api"
    __method__ = "api/v3/warehouses"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    name: str = Field(None)
    office_id: int = Field(None, alias="officeId")
