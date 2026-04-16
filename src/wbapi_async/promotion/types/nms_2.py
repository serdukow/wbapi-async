from pydantic import Field

from ...types.base import BaseType


class Nms2(BaseType):
    """Product cards"""

    added: list[int] = Field(alias="added")
    deleted: list[int] = Field(alias="deleted")
