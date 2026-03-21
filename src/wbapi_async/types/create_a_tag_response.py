from typing import Any

from pydantic import Field

from .base import BaseType


class CreateATagResponse(BaseType):
    """Create a Tag"""

    data: dict[str, Any] | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: str | None = Field(None, alias="additionalErrors")
