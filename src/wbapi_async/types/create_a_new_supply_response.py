from pydantic import Field

from .base import BaseType


class CreateANewSupplyResponse(BaseType):
    """Create a New Supply"""

    id: str | None = Field(None)
