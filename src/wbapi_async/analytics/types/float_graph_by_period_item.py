from pydantic import Field

from ...types.base import BaseType


class FloatGraphByPeriodItem(BaseType):
    """Average monthly orders"""

    start: str = Field(alias="start")
    end: str = Field(alias="end")
    value: float = Field(alias="value")
