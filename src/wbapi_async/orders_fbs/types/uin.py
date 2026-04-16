from pydantic import Field

from ...types.base import BaseType


class Uin(BaseType):
    """UIN"""

    value: str | None = Field(None)
