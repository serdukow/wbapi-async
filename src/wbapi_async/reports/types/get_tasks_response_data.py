from pydantic import Field

from ...types.base import BaseType


class GetTasksResponseData(BaseType):
    id_: str | None = Field(None, alias="id")
    status: str | None = Field(None, alias="status")
