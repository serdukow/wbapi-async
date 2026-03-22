from typing import Any

from pydantic import Field

from ...types.base import BaseType


class AddProductToThePromotionResponse(BaseType):
    """Add Product to the Promotion"""

    data: dict[str, Any] | None = Field(None)
