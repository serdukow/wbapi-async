from pydantic import Field

from ...methods.base import WbMethod
from ...types import DetailsForTheAcquiringExpensesReportsByReportIdResponse, RequestLimit


class DetailsForTheAcquiringExpensesReportsByReportId(WbMethod):
    """
    Method is available by token types : Personal , Service

    Source: https://dev.wildberries.ru/en/docs/openapi/financial-reports-and-accounting#tag/Financial-Reports/paths/~1api~1finance~1v1~1acquiring~1detailed~1%7BreportId%7D/post
    """

    __return__ = DetailsForTheAcquiringExpensesReportsByReportIdResponse
    __api__ = "finance-api"
    __method__ = ""
    __method_template__ = "api/finance/v1/acquiring/detailed/{report_id}"
    __http_method__ = "POST"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    report_id: int = Field(alias="reportId", exclude=True)
    limit: int | None = Field(100000)
    rrd_id: int | None = Field(0, alias="rrdId")
    fields: list[str] | None = Field(None)
