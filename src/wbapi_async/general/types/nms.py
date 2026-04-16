from typing import Any

from pydantic import Field

from ...types.base import BaseType


class Nms(BaseType):
    """Product cards. Maximum of 50 products per campaign"""

    add: Any | None = Field(None)
    delete: list[int] | None = Field(None)
