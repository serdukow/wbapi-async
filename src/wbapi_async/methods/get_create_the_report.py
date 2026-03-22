from pydantic import Field

from ..types.create_the_report_response import CreateTheReportResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetCreateTheReport(WbMethod):
    """
    Creates a task for report generation.<br></br>

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Acceptance-Expenses/paths/~1api~1v1~1acceptance_report/get
    """

    __return__ = CreateTheReportResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/acceptance_report"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=1)

    date_from: str = Field(None, alias="dateFrom")
    date_to: str = Field(None, alias="dateTo")
