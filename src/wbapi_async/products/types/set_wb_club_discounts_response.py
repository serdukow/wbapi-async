from typing import Any

from pydantic import Field

from ...types.base import BaseType


class SetWbClubDiscountsResponse(BaseType):
    """Set WB Club Discounts"""

    data: dict[str, Any] | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
