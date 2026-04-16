from pydantic import Field

from ...types.base import BaseType


class CreateANewSupplyResponse(BaseType):
    """Create a New Supply"""

    id_: str | None = Field(None, alias="id")
