from pydantic import Field

from ...types.base import BaseType
from .create_task_response_data import CreateTaskResponseData


class GenerateTheReportResponse(BaseType):
    """Generate the Report"""

    data: CreateTaskResponseData | None = Field(None, alias="data")
