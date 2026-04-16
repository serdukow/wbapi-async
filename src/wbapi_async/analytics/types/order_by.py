from pydantic import Field

from ...types.base import BaseType


class OrderBy(BaseType):
    """Sorting parameters"""

    field: str = Field(alias="field")
    mode: str = Field(alias="mode")
