from pydantic import Field

from ..types.regenerate_the_report_response import RegenerateTheReportResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class RegenerateTheReport(WbMethod):
    """
    The method creates a [repeated generation
    task](/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/post)of
    reportwith advanced seller analytics. This is necessary if you [received the
    status](/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/get)
    `FAILED`when generating the report.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads~1retry/post
    """

    __return__ = RegenerateTheReportResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v2/nm-report/downloads/retry"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=3, interval=20, burst=3)

    download_id: str | None = Field(None, alias="downloadId")
