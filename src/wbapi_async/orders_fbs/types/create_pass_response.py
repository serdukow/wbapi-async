from pydantic import Field

from ...types.base import BaseType


class CreatePassResponse(BaseType):
    """Create Pass"""

    id: int | None = Field(None)
