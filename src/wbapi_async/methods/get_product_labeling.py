from pydantic import Field

from ..types.product_labeling_item import ProductLabelingItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetProductLabeling(WbMethod):
    """
    Returns a report on deductions for the absence of mandatory product labeling.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Retention-Reports/paths/~1api~1v1~1analytics~1goods-labeling/get
    """

    __return__ = ProductLabelingItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/goods-labeling"
    __data_key__ = "report"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=10)

    date_from: str = Field(None, alias="dateFrom")
    date_to: str = Field(None, alias="dateTo")
