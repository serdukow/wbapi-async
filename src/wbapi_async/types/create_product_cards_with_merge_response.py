from typing import Any

from pydantic import Field

from .base import BaseType


class CreateProductCardsWithMergeResponse(BaseType):
    """Create Product Cards with Merge"""

    data: dict[str, Any] | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: Any | None = Field(None, alias="additionalErrors")
