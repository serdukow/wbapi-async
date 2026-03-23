from pydantic import Field

from ...types.base import BaseType


class OfficesForPassResponse(BaseType):
    """Get Offices for Pass"""

    name: str | None = Field(None)
    address: str | None = Field(None)
    id_: int | None = Field(None, alias="id")
