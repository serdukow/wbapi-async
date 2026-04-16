from pydantic import Field

from ...types.base import BaseType


class TypesItem(BaseType):
    id_: int | None = Field(None, alias="id")
    name: str | None = Field(None)
