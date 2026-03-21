from typing import Any

from pydantic import Field

from ..types.request_limit import RequestLimit
from ..types.update_inventory_response import UpdateInventoryResponse
from .base import WbMethod


class UpdateInventory(WbMethod):
    """
    Updates product inventory.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses-Inventory/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/put
    """

    __return__ = UpdateInventoryResponse
    __empty_response__ = True
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/stocks/{warehouse_id}"
    __http_method__ = "PUT"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    warehouse_id: int = Field(alias="warehouseId", exclude=True)
    stocks: list[dict[str, Any]] = Field(None)
