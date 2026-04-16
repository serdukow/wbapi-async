from pydantic import Field

from ...types.base import BaseType


class Nms(BaseType):
    """Product cards. Maximum of 50 products per campaign"""

    add: list[int] | None = Field(None, alias="add")
    delete: list[int] | None = Field(None, alias="delete")
