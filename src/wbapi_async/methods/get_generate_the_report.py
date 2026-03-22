from pydantic import Field

from ..types.generate_the_report_response import GenerateTheReportResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetGenerateTheReport(WbMethod):
    """
    Create a task to generate a report. Maximum of report period — 8 days

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Paid-Storage/paths/~1api~1v1~1paid_storage/get
    """

    __return__ = GenerateTheReportResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/paid_storage"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=5)

    date_from: str = Field(None, alias="dateFrom")
    date_to: str = Field(None, alias="dateTo")
