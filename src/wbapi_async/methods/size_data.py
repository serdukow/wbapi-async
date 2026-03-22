from ..types.size_data_item import SizeDataItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class SizeData(WbMethod):
    """
    Forms a dataset for inventory by the size of the product.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1sizes/post
    """

    __return__ = SizeDataItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/stocks-report/products/sizes"
    __http_method__ = "POST"
    __data_key__ = "data.offices"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)
