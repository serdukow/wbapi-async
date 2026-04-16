from pydantic import Field

from ...types.base import BaseType
from .data_2 import Data2


class SetWbClubDiscountsResponse(BaseType):
    """Set WB Club Discounts"""

    data: Data2 | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
