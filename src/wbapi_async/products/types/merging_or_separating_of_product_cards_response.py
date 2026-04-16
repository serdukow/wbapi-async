from typing import Any

from pydantic import Field

from ...types.base import BaseType


class MergingOrSeparatingOfProductCardsResponse(BaseType):
    """Merging or Separating of Product Cards"""

    data: dict[str, Any] | None = Field(None, alias="data")
    error: bool | None = Field(None, alias="error")
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: Any | None = Field(None, alias="additionalErrors")
