from pydantic import Field

from ...enums import Period
from ...methods.base import WbMethod
from ...types import RequestLimit, SalesReportListResponse


class SalesReportList(WbMethod):
    """
    Method is available by token types : Personal , Service

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Financial-Reports/paths/~1api~1finance~1v1~1sales-reports~1list/post
    """

    __return__ = SalesReportListResponse
    __api__ = "finance-api"
    __method__ = "api/finance/v1/sales-reports/list"
    __http_method__ = "POST"
    __pagination__ = "offset"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    limit: int | None = Field(1000)
    offset: int | None = Field(0)
    period: Period | None = Field(Period.WEEKLY)
