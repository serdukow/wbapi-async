from pydantic import Field

from ...types.base import BaseType


class Wholesale(BaseType):
    """Wholesale"""

    enabled: bool | None = Field(None)
    quantum: float | None = Field(None)
