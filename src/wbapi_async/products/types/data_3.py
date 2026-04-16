from pydantic import Field

from ...types.base import BaseType


class Data3(BaseType):
    """Response data"""

    id_: int | None = Field(None, alias="id")
    already_exists: bool | None = Field(None, alias="alreadyExists")
