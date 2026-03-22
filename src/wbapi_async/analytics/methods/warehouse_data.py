from ...methods.base import WbMethod
from ...types import RequestLimit, WarehouseDataItem


class WarehouseData(WbMethod):
    """
    Forms a dataset for inventory by warehouses. The data on the seller's warehouses are in an
    aggregatedform — for all of them together without detailing specific warehouses — and responses
    contain`"regionName":"Маркетплейс"` and `"offices":[]`.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1offices/post
    """

    __return__ = WarehouseDataItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/stocks-report/offices"
    __http_method__ = "POST"
    __data_key__ = "data.regions"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
