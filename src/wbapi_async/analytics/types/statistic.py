from pydantic import Field

from ...types.base import BaseType
from .comparison import Comparison
from .selected import Selected


class Statistic(BaseType):
    selected: Selected = Field(alias="selected")
    past: Selected | None = Field(None, alias="past")
    comparison: Comparison | None = Field(None, alias="comparison")
