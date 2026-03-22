from pydantic import Field

from ..types.realization_sales_report_response import RealizationSalesReportResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetRealizationSalesReport(WbMethod):
    """
    Details for the [realization
    reports](https://seller.wildberries.ru/suppliers-mutual-settlements).

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Financial-Reports/paths/~1api~1v5~1supplier~1reportDetailByPeriod/get
    """

    __return__ = RealizationSalesReportResponse
    __api__ = "statistics-api"
    __method__ = "api/v5/supplier/reportDetailByPeriod"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=1, burst=1)

    date_from: str = Field(None, alias="dateFrom")
    date_to: str = Field(None, alias="dateTo")
    limit: int | None = Field(100000)
    rrdid: int | None = Field(0)
    period: str | None = Field("weekly")
