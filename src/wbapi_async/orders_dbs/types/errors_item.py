from pydantic import Field

from ...types.base import BaseType


class ErrorsItem(BaseType):
    code: int | None = Field(None)
    detail: str | None = Field(None)
