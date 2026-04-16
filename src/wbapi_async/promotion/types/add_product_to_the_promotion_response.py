from pydantic import Field

from ...products.types.data import Data
from ...types.base import BaseType


class AddProductToThePromotionResponse(BaseType):
    """Add Product to the Promotion"""

    data: Data | None = Field(None)
