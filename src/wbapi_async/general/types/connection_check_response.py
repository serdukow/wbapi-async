from pydantic import Field

from ...types.base import BaseType
from ..enums.status import Status


class ConnectionCheckResponse(BaseType):
    """Connection Check"""

    ts: str | None = Field(None, alias="TS")
    status: Status | None = Field(None, alias="Status")
