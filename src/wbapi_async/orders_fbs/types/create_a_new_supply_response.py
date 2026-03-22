from pydantic import Field

from ...types.base import BaseType


class CreateANewSupplyResponse(BaseType):
    """Create a New Supply"""

    id: str | None = Field(None)
