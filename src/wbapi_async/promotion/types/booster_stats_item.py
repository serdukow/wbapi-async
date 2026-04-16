from pydantic import Field

from ...types.base import BaseType


class BoosterStatsItem(BaseType):
    avg_position: int = Field()
    date: str = Field()
    nm: int = Field()
