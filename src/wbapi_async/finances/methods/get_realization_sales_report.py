from pydantic import Field

from ...methods.base import WbMethod
from ...types import RealizationSalesReportResponse, RequestLimit
from ..enums.period import Period


class GetRealizationSalesReport(WbMethod):
    """
    Details for the [realization
    reports](https://seller.wildberries.ru/suppliers-mutual-settlements).The report contains data
    since29 January 2024.

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Financial-Reports/paths/~1api~1v5~1supplier~1reportDetailByPeriod/get
    """

    __return__ = RealizationSalesReportResponse
    __api__ = "statistics-api"
    __method__ = "api/v5/supplier/reportDetailByPeriod"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    limit: int | None = Field(100000)
    rrdid: int | None = Field(0)
    period: Period | None = Field(Period.WEEKLY)
