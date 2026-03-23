from pydantic import Field

from ...types import GenerateTheReportResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetGenerateTheReport(WbMethod):
    """
    Create a task to generate a report. Maximum of report period — 8 days

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Paid-Storage/paths/~1api~1v1~1paid_storage/get
    """

    __return__ = GenerateTheReportResponse
    __api__ = "seller-analytics-api"
    __method__ = "api/v1/paid_storage"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
