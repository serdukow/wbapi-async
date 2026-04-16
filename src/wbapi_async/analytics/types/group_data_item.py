from pydantic import Field

from ...types.base import BaseType
from .metrics import Metrics
from .table_product_item_st import TableProductItemSt


class GroupDataItem(BaseType):
    """Group Data"""

    subject_id: int = Field(alias="subjectID")
    subject_name: str = Field(alias="subjectName")
    brand_name: str = Field(alias="brandName")
    tag_id: int = Field(alias="tagID")
    tag_name: str = Field(alias="tagName")
    metrics: Metrics = Field(alias="metrics")
    items: list[TableProductItemSt] = Field(alias="items")
