from typing import Any

from pydantic import Field

from .base import BaseType


class SetPricesAndDiscountsResponse(BaseType):
    """Set Prices and Discounts"""

    data: dict[str, Any] | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
