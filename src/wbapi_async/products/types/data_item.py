from pydantic import Field

from ...types.base import BaseType


class DataItem(BaseType):
    name: str | None = Field(None)
    id_: int | None = Field(None, alias="id")
    is_visible: bool | None = Field(None, alias="isVisible")
