from pydantic import Field

from ...enums import Period
from ...methods.base import WbMethod
from ...types import DetailsForTheSalesReportsByPeriodResponse, RequestLimit


class DetailsForTheSalesReportsByPeriod(WbMethod):
    """
    The method returns details for the [sales
    reports](https://seller.wildberries.ru/suppliers-mutual-settlements)by specified period. The
    datais available since January 29, 2024.

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Financial-Reports/paths/~1api~1finance~1v1~1sales-reports~1detailed/post
    """

    __return__ = DetailsForTheSalesReportsByPeriodResponse
    __api__ = "finance-api"
    __method__ = "api/finance/v1/sales-reports/detailed"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    limit: int | None = Field(100000)
    rrd_id: int | None = Field(0, alias="rrdId")
    period: Period | None = Field(Period.WEEKLY)
    fields: list[str] | None = Field(None)
