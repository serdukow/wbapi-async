from pydantic import Field

from ...methods.base import WbMethod
from ...types import RequestLimit, WarehouseRemainsTasksTaskIdDownloadResponse


class GetWarehouseRemainsTasksTaskIdDownload(WbMethod):
    """
    Returns the report by task ID

    Source: https://dev.wildberries.ru/en/docs/openapi/reports#tag/Warehouses-Inventory-Report/paths/~1api~1v1~1warehouse_remains~1tasks~1%7Btask_id%7D~1download/get
    """

    __return__ = WarehouseRemainsTasksTaskIdDownloadResponse
    __api__ = "seller-analytics-api"
    __method__ = ""
    __method_template__ = "api/v1/warehouse_remains/tasks/{task_id}/download"

    request_limit: RequestLimit = RequestLimit(period=60, limit=10, interval=600, burst=5)

    task_id: str = Field(alias="task_id", exclude=True)
