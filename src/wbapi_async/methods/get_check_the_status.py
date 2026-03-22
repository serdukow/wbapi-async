from pydantic import Field

from ..types.check_the_status_response import CheckTheStatusResponse
from ..types.request_limit import RequestLimit
from .base import WbMethod


class GetCheckTheStatus(WbMethod):
    """
    Returns the status of task

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Paid-Storage/paths/~1api~1v1~1paid_storage~1tasks~1%7Btask_id%7D~1status/get
    """

    __return__ = CheckTheStatusResponse
    __api__ = "seller-analytics-api"
    __method__ = ""
    __method_template__ = "api/v1/paid_storage/tasks/{task_id}/status"

    request_limit: RequestLimit = RequestLimit(period=5, limit=1, interval=5, burst=5)

    task_id: str = Field(exclude=True)
