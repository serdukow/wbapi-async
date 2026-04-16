from pydantic import Field

from ...types.base import BaseType
from .data import Data


class LimitsForTheProductCardsResponse(BaseType):
    """Limits for the Product Cards"""

    data: Data | None = Field(None, alias="data")
    error: bool | None = Field(None, alias="error")
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: str | None = Field(None, alias="additionalErrors")
