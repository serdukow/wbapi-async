from pydantic import Field

from ...types.base import BaseType


class Adverts(BaseType):
    type_: int | None = Field(None, alias="type")
    status: int | None = Field(None)
    count: int | None = Field(None)
