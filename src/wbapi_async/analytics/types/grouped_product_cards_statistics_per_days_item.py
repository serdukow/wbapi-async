from pydantic import Field

from ...types.base import BaseType
from .history import History
from .product import Product


class GroupedProductCardsStatisticsPerDaysItem(BaseType):
    """Grouped Product Cards Statistics per Days"""

    product: Product = Field()
    history: list[History] = Field()
    currency: str = Field()
