from pydantic import Field

from ..types.inventory_item import InventoryItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetInventory(WbMethod):
    """
    Returns product inventory.

    Source: https://dev.wildberries.ru/en/docs/openapi/work-with-products#tag/Seller-Warehouses-Inventory/paths/~1api~1v3~1stocks~1%7BwarehouseId%7D/post
    """

    __return__ = InventoryItem
    __api__ = "marketplace-api"
    __method__ = ""
    __method_template__ = "api/v3/stocks/{warehouse_id}"
    __http_method__ = "POST"
    __data_key__ = "stocks"

    request_limit: RequestLimit = RequestLimit(period=60, limit=300, interval=200, burst=20)

    warehouse_id: int = Field(alias="warehouseId", exclude=True)
    chrt_ids: list[int] = Field(None, alias="chrtIds")
