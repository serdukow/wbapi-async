from pydantic import Field

from ...types.base import BaseType
from .data import Data


class SetWbClubDiscountsResponse(BaseType):
    """Set WB Club Discounts"""

    data: Data | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
