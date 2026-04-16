from pydantic import Field

from ...types.base import BaseType


class ApiBatchErrorResponse(BaseType):
    code: int | None = Field(None, alias="code")
    detail: str | None = Field(None, alias="detail")
