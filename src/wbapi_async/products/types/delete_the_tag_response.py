from typing import Any

from pydantic import Field

from ...types.base import BaseType


class DeleteTheTagResponse(BaseType):
    """Delete the Tag"""

    data: dict[str, Any] | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: str | None = Field(None, alias="additionalErrors")
