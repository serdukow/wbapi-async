from pydantic import Field

from ...methods.base import WbMethod
from ...types import AcceptanceReportResponse, RequestLimit


class GetAcceptanceReport(WbMethod):
    """
    Creates a task for report generation. Maximum of report period is 31 days.

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Acceptance-Expenses/paths/~1api~1v1~1acceptance_report/get
    """

    __return__ = AcceptanceReportResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/acceptance_report"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
