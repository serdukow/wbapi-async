from pydantic import Field

from ...types.base import BaseType


class RangingItem(BaseType):
    condition: str | None = Field(None)
    participation_rate: int | None = Field(None, alias="participationRate")
    boost: int | None = Field(None)
