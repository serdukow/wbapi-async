from typing import Any

from pydantic import Field

from ...types.base import BaseType


class UpdateTheTagResponse(BaseType):
    """Update the Tag"""

    data: dict[str, Any] | None = Field(None, alias="data")
    error: bool | None = Field(None, alias="error")
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: str | None = Field(None, alias="additionalErrors")
