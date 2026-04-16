from pydantic import Field

from ...types.base import BaseType


class Gtin(BaseType):
    """GTIN"""

    value: str | None = Field(None)
