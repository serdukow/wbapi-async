from pydantic import Field

from ..types.report_item import ReportItem
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetReport(WbMethod):
    """
    Returns a list of [goods returns to the
    seller](https://seller.wildberries.ru/analytics-reports/goods-return).With one request, you can
    obtaina report for a maximum of 31 days.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Returns-and-Product-Movement-Report/paths/~1api~1v1~1analytics~1goods-return/get
    """

    __return__ = ReportItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/goods-return"
    __data_key__ = "report"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=10)

    date_from: str = Field(None, alias="dateFrom")
    date_to: str = Field(None, alias="dateTo")
