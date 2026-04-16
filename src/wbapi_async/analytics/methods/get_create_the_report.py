from ...methods.base import WbMethod
from ...types import CreateTheReportResponse, RequestLimit


class GetCreateTheReport(WbMethod):
    """
    The method creates a task for generating a report with advanced seller analytics. You can
    createa CSV-version of [sales funnel](/openapi/analytics#tag/Sales-Funnel) or [search
    parameters](/openapi/analytics#tag/Search-Queries-for-Your-Items)report with grouping:

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/post
    """

    __return__ = CreateTheReportResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/nm-report/downloads"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)
