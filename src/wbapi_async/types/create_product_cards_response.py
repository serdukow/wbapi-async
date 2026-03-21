from typing import Any

from pydantic import Field

from .base import BaseType


class CreateProductCardsResponse(BaseType):
    """Create Product Cards"""

    data: dict[str, Any] | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: Any | None = Field(None, alias="additionalErrors")
