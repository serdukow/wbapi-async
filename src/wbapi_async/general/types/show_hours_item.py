from pydantic import Field

from ...types.base import BaseType


class ShowHoursItem(BaseType):
    from_: int | None = Field(None, alias="From")
    to: int | None = Field(None, alias="To")
