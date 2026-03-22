from typing import Any

from pydantic import Field

from ...types.base import BaseType


class GroupedProductCardsStatisticsPerDaysItem(BaseType):
    """Grouped Product Cards Statistics per Days"""

    product: Any = Field()
    history: list[Any] = Field()
    currency: str = Field()
