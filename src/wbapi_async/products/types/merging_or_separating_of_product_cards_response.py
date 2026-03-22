from typing import Any

from pydantic import Field

from ...types.base import BaseType


class MergingOrSeparatingOfProductCardsResponse(BaseType):
    """Merging or Separating of Product Cards"""

    data: dict[str, Any] | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: Any | None = Field(None, alias="additionalErrors")
