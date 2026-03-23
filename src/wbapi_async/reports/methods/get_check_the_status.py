from pydantic import Field

from ...types import CheckTheStatusResponse
from ...types import RequestLimit
from ...methods.base import WbMethod


class GetCheckTheStatus(WbMethod):
    """
    Returns the status of the generation task

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Warehouses-Inventory-Report/paths/~1api~1v1~1warehouse_remains~1tasks~1%7Btask_id%7D~1status/get
    """

    __return__ = CheckTheStatusResponse
    __api__ = "seller-analytics-api"
    __method__ = ""
    __method_template__ = "api/v1/warehouse_remains/tasks/{task_id}/status"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    task_id: str = Field(exclude=True)
