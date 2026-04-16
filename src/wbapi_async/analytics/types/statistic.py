from pydantic import Field

from ...types.base import BaseType
from .comparison import Comparison
from .selected import Selected


class Statistic(BaseType):
    selected: Selected = Field()
    past: Selected | None = Field(None)
    comparison: Comparison | None = Field(None)
