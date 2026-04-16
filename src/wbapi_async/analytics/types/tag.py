from pydantic import Field

from ...types.base import BaseType


class Tag(BaseType):
    """Tag"""

    id_: int = Field(alias="id")
    name: str = Field()
