from ..types.product_data_item import ProductDataItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class ProductData(WbMethod):
    """
    Forms a dataset for inventory by products.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1products/post
    """

    __return__ = ProductDataItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/stocks-report/products/products"
    __http_method__ = "POST"
    __data_key__ = "data.items"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)
