from pydantic import Field

from ..enums.realization_sales_report_period import RealizationSalesReportPeriod
from ..types.realization_sales_report import RealizationSalesReport
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetRealizationSalesReport(WbMethod):
    """
    Details for the realization reports.

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Financial-Reports/paths/~1api~1v5~1supplier~1reportDetailByPeriod/get
    """

    __return__ = RealizationSalesReport
    __api__ = "statistics-api"
    __method__ = "api/v5/supplier/reportDetailByPeriod"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=1)

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    limit: int = Field(100000, alias="limit")
    rrdid: int = Field(0, alias="rrdid")
    period: RealizationSalesReportPeriod = Field(
        RealizationSalesReportPeriod.WEEKLY, alias="period"
    )
