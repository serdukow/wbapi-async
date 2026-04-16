from pydantic import Field

from ...types.base import BaseType
from .answer import Answer
from .product_details import ProductDetails


class QuestionListItem(BaseType):
    """Question List"""

    id_: str | None = Field(None, alias="id")
    text: str | None = Field(None)
    created_date: str | None = Field(None, alias="createdDate")
    state: str | None = Field(None)
    answer: Answer | None = Field(None)
    product_details: ProductDetails | None = Field(None, alias="productDetails")
    was_viewed: bool | None = Field(None, alias="wasViewed")
    is_warned: bool | None = Field(None, alias="isWarned")
