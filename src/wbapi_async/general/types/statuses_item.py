from pydantic import Field

from ...types.base import BaseType


class StatusesItem(BaseType):
    date: str | None = Field(None)
    code: str | None = Field(None)
