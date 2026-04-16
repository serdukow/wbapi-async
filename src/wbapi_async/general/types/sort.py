from pydantic import Field

from ...types.base import BaseType


class Sort(BaseType):
    """Sort by"""

    ascending: bool | None = Field(None)
