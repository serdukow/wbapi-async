from pydantic import Field

from ...types.base import BaseType


class FloatGraphByPeriodItem(BaseType):
    """Average monthly orders"""

    start: str = Field()
    end: str = Field()
    value: float = Field()
