from pydantic import Field

from .base import BaseType


class ConnectionCheckResponse(BaseType):
    """Connection Check"""

    ts: str | None = Field(None, alias="TS")
    status: str | None = Field(None, alias="Status")
