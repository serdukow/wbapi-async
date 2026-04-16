from pydantic import Field

from ...types.base import BaseType
from .data import Data


class LimitsForTheProductCardsResponse(BaseType):
    """Limits for the Product Cards"""

    data: Data | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: str | None = Field(None, alias="additionalErrors")
