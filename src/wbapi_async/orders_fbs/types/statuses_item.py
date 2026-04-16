from pydantic import Field

from ...types.base import BaseType


class StatusesItem(BaseType):
    date: str | None = Field(None, alias="date")
    code: str | None = Field(None, alias="code")
