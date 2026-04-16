from pydantic import Field

from ...types.base import BaseType


class Options2(BaseType):
    """Order options"""

    is_b2b: bool | None = Field(None, alias="isB2b")
