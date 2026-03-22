from pydantic import Field

from .base import BaseType


class CreatePassResponse(BaseType):
    """Create Pass"""

    id: int | None = Field(None)
