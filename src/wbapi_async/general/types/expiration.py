from pydantic import Field

from ...types.base import BaseType


class Expiration(BaseType):
    """Expiration date"""

    value: str | None = Field(None)
