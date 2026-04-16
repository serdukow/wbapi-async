from pydantic import Field

from ...types.base import BaseType
from .data_item import DataItem


class ProductsParentCategoriesResponse(BaseType):
    """Products Parent Categories"""

    data: list[DataItem] | None = Field(None, alias="data")
    error: bool | None = Field(None, alias="error")
    error_text: str | None = Field(None, alias="errorText")
    additional_errors: str | None = Field(None, alias="additionalErrors")
