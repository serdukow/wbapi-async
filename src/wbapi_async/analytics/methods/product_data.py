from ...methods.base import WbMethod
from ...types import ProductDataItem, RequestLimit


class ProductData(WbMethod):
    """
    Forms a dataset for inventory by products. You can get data for individual products as well as
    forthe entire report if there are no filters in the query: `nmIDs`, `subjectID`, `brandName`,
    `tagID`.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Stocks-Report/paths/~1api~1v2~1stocks-report~1products~1products/post
    """

    __return__ = ProductDataItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/stocks-report/products/products"
    __http_method__ = "POST"
    __data_key__ = "data.items"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
