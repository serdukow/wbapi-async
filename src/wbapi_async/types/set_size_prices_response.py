from typing import Any

from pydantic import Field

from .base import BaseType


class SetSizePricesResponse(BaseType):
    """Set Size Prices"""

    data: dict[str, Any] | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
