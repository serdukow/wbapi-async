from pydantic import Field

from ...types.base import BaseType
from .data_2 import Data2


class SetSizePricesResponse(BaseType):
    """Set Size Prices"""

    data: Data2 | None = Field(None, alias="data")
    error: bool | None = Field(None, alias="error")
    error_text: str | None = Field(None, alias="errorText")
