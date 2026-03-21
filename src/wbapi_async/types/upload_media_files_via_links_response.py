from typing import Any

from pydantic import Field

from .base import BaseType


class UploadMediaFilesViaLinksResponse(BaseType):
    """Upload Media Files via Links"""

    data: dict[str, Any] | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: dict[str, Any] | None = Field(None, alias="additionalErrors")
