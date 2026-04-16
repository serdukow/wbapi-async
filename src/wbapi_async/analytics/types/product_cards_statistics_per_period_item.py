from pydantic import Field

from ...types.base import BaseType
from .product import Product
from .statistic import Statistic


class ProductCardsStatisticsPerPeriodItem(BaseType):
    """Product Cards Statistics per Period"""

    product: Product = Field(alias="product")
    statistic: Statistic = Field(alias="statistic")
