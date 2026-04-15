from pydantic import Field

from ...types.base import BaseType
from ..enums.product_data_order_field import ProductDataOrderField
from ..enums.product_data_order_mode import ProductDataOrderMode


class ProductDataOrderBy(BaseType):
    """Sorting parameters for product data"""

    field: ProductDataOrderField = Field()
    mode: ProductDataOrderMode = Field()
