from ..types.warehouse_data_item import WarehouseDataItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class WarehouseData(WbMethod):
    """
    Forms a dataset for inventory by warehouses.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1offices/post
    """

    __return__ = WarehouseDataItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/stocks-report/offices"
    __http_method__ = "POST"
    __data_key__ = "data.regions"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)
