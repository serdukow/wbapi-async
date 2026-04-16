from typing import Any

from pydantic import Field

from ...types.base import BaseType


class CharacteristicsItem(BaseType):
    id_: int | None = Field(None, alias="id")
    name: str | None = Field(None, alias="name")
    value: Any | None = Field(None, alias="value")
