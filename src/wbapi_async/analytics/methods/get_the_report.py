from pydantic import Field

from ...types import RequestLimit
from ...types import TheReportResponse
from ...methods.base import WbMethod


class GetTheReport(WbMethod):
    """
    The method provides a report with advanced seller analytics by [generation
    task](/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads/post)
    ID.You can get a report that was generated within the last 48 hours. The report will be
    downloadedinside a ZIP archive in CSV format.

    Source: https://dev.wildberries.ru/en/docs/openapi/analytics#tag/Seller-Analytics-CSV/paths/~1api~1v2~1nm-report~1downloads~1file~1%7BdownloadId%7D/get
    """

    __return__ = TheReportResponse
    __empty_response__ = True
    __api__ = "seller-analytics-api"
    __method__ = ""
    __method_template__ = "api/v2/nm-report/downloads/file/{download_id}"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    download_id: str = Field(alias="downloadId", exclude=True)
