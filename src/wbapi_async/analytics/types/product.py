from pydantic import Field

from ...types.base import BaseType
from .stocks import Stocks
from .tag import Tag


class Product(BaseType):
    nm_id: int = Field(alias="nmId")
    title: str = Field(alias="title")
    vendor_code: str = Field(alias="vendorCode")
    brand_name: str = Field(alias="brandName")
    subject_id: int = Field(alias="subjectId")
    subject_name: str = Field(alias="subjectName")
    tags: list[Tag] = Field(alias="tags")
    product_rating: float = Field(alias="productRating")
    feedback_rating: float = Field(alias="feedbackRating")
    stocks: Stocks = Field(alias="stocks")
