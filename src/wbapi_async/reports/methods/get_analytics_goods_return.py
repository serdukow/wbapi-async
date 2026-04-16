from pydantic import Field

from ...methods.base import WbMethod
from ...types import AnalyticsGoodsReturnItem, RequestLimit


class GetAnalyticsGoodsReturn(WbMethod):
    """
    Returns a list of [goods returns to the
    seller](https://seller.wildberries.ru/analytics-reports/goods-return).With one request, you can
    obtaina report for a maximum of 31 days.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Returns-and-Product-Movement-Report/paths/~1api~1v1~1analytics~1goods-return/get
    """

    __return__ = AnalyticsGoodsReturnItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/goods-return"
    __data_key__ = "report"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
