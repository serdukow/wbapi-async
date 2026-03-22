from pydantic import Field

from ..types.the_report_response import TheReportResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetTheReport(WbMethod):
    """
    Returns the report by task ID

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Paid-Storage/paths/~1api~1v1~1paid_storage~1tasks~1%7Btask_id%7D~1download/get
    """

    __return__ = TheReportResponse
    __api__ = "seller-analytics-api"
    __method__ = ""
    __method_template__ = "api/v1/paid_storage/tasks/{task_id}/download"

    request_limit: RequestLimit = RequestLimit(period=60, limit=1, interval=60000, burst=1)

    task_id: str = Field(exclude=True)
