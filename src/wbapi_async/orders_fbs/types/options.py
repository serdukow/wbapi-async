from pydantic import Field

from ...types.base import BaseType


class Options(BaseType):
    """Order options"""

    is_b2_b: bool | None = Field(None, alias="isB2B")
