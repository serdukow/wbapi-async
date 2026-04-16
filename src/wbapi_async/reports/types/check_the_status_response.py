from pydantic import Field

from ...types.base import BaseType
from .get_tasks_response_data import GetTasksResponseData


class CheckTheStatusResponse(BaseType):
    """Check the Status"""

    data: GetTasksResponseData | None = Field(None)
