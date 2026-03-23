from pydantic import Field

from ...types import ReportItem
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetReport(WbMethod):
    """
    Returns sales data grouped by regions of the countries. You can obtain a report for a maximum
    of31 days.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Sales-by-Regions/paths/~1api~1v1~1analytics~1region-sale/get
    """

    __return__ = ReportItem
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/analytics/region-sale"
    __data_key__ = "report"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
