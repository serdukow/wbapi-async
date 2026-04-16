from pydantic import Field

from ...types.base import BaseType


class AdvertSubject(BaseType):
    """Subject"""

    id_: int = Field(alias="id")
    name: str = Field(alias="name")
