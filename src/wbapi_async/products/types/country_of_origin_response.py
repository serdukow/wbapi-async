from pydantic import Field

from ...types.base import BaseType
from .data_item import DataItem


class CountryOfOriginResponse(BaseType):
    """Country of Origin"""

    data: list[DataItem] | None = Field(None)
    error: bool | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: str | None = Field(None, alias="additionalErrors")
