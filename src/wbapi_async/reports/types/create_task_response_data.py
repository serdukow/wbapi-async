from pydantic import Field

from ...types.base import BaseType


class CreateTaskResponseData(BaseType):
    task_id: str | None = Field(None, alias="taskId")
