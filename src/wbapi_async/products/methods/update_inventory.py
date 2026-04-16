from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, StocksItem, UpdateInventoryResponse


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

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    warehouse_id: int = Field(alias="warehouseId", exclude=True)
    stocks: list[StocksItem] = Field()
