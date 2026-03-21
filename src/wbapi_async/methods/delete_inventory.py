from pydantic import Field

from ..types.delete_inventory_response import DeleteInventoryResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class DeleteInventory(WbMethod):
    """
    Deletes product inventory.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses-Inventory/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/delete
    """

    __return__ = DeleteInventoryResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/stocks/{warehouse_id}"
    __http_method__ = "DELETE"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=6, burst=2)

    warehouse_id: int = Field(alias="warehouseId", exclude=True)
    chrt_ids: list[int] = Field(None, alias="chrtIds")
