from pydantic import Field

from ...types import InventoryItem
from ...types import RequestLimit
from ...methods.base import WbMethod


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    warehouse_id: int = Field(alias="warehouseId", exclude=True)
    chrt_ids: list[int] = Field(alias="chrtIds")
