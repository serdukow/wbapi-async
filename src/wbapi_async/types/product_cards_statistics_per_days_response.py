from typing import Any

from pydantic import Field

from .base import BaseType


class ProductCardsStatisticsPerDaysResponse(BaseType):
    """Product Cards Statistics per Days"""

    product: Any = Field(None)
    history: list[Any] = Field(None)
    currency: str = Field(None)
