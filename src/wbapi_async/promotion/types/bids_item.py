from pydantic import Field

from ...types.base import BaseType


class BidsItem(BaseType):
    type_: str = Field(alias="type")
    value: int = Field(alias="value")
