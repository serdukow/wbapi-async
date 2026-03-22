from typing import Any

from pydantic import Field

from ...types.base import BaseType


class ProductCardsStatisticsPerPeriodResponse(BaseType):
    """Product Cards Statistics per Period"""

    data: Any = Field()
