from pydantic import Field

from ...methods.base import WbMethod
from ...types import ProductLabelingItem, RequestLimit


class GetProductLabeling(WbMethod):
    """
    Returns a report on deductions for the absence of mandatory product labeling. The report
    containsphotos of products where the labeling is absent or cannot be read. Data can be obtained
    forup to 31 days, starting from March 2024

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1v1~1analytics~1goods-labeling/get
    """

    __return__ = ProductLabelingItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/goods-labeling"
    __data_key__ = "report"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
