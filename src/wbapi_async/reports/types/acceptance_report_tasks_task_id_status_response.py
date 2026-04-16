from pydantic import Field

from ...types.base import BaseType
from .get_tasks_response_data import GetTasksResponseData


class AcceptanceReportTasksTaskIdStatusResponse(BaseType):
    """Check the Status"""

    data: GetTasksResponseData | None = Field(None, alias="data")
