from pydantic import Field

from .base import BaseType


class ConnectionCheck(BaseType):
    ts: str | None = Field(None, alias="TS")
    status: str | None = Field(None, alias="Status")
