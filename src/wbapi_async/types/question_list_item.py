from typing import Any

from pydantic import Field

from .base import BaseType


class QuestionListItem(BaseType):
    """Question List"""

    id: str | None = Field(None)
    text: str | None = Field(None)
    created_date: str | None = Field(None, alias="createdDate")
    state: str | None = Field(None)
    answer: dict[str, Any] | None = Field(None)
    product_details: dict[str, Any] | None = Field(None, alias="productDetails")
    was_viewed: bool | None = Field(None, alias="wasViewed")
    is_warned: bool | None = Field(None, alias="isWarned")
