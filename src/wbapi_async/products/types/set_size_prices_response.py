from pydantic import Field

from ...types.base import BaseType
from .data import Data


class SetSizePricesResponse(BaseType):
    """Set Size Prices"""

    data: Data | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
