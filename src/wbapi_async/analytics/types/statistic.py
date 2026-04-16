from pydantic import Field

from ...types.base import BaseType
from .comparison import Comparison
from .past import Past
from .selected import Selected


class Statistic(BaseType):
    selected: Selected = Field()
    past: Past | None = Field(None)
    comparison: Comparison | None = Field(None)
