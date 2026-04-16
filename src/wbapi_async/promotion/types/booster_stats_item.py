from pydantic import Field

from ...types.base import BaseType


class BoosterStatsItem(BaseType):
    avg_position: int = Field(alias="avg_position")
    date: str = Field(alias="date")
    nm: int = Field(alias="nm")
