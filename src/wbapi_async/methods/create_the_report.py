from ..types.create_the_report_response import CreateTheReportResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class CreateTheReport(WbMethod):
    """
    The method creates a task for generating a report with advanced seller analytics.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/post
    """

    __return__ = CreateTheReportResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/nm-report/downloads"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)
