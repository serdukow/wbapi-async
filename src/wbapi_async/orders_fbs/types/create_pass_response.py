from pydantic import Field

from ...types.base import BaseType


class CreatePassResponse(BaseType):
    """Create Pass"""

    id_: int | None = Field(None, alias="id")
