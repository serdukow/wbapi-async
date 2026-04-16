from pydantic import Field

from ...types.base import BaseType
from .data_3 import Data3


class AddProductToThePromotionResponse(BaseType):
    """Add Product to the Promotion"""

    data: Data3 | None = Field(None)
