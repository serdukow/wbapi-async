from typing import Any

from pydantic import Field

from .base import BaseType


class ProductDataItem(BaseType):
    """Product Data"""

    nm_id: int = Field(None, alias="nmID")
    is_deleted: bool = Field(None, alias="isDeleted")
    subject_name: str = Field(None, alias="subjectName")
    name: str = Field(None)
    vendor_code: str = Field(None, alias="vendorCode")
    brand_name: str = Field(None, alias="brandName")
    main_photo: str = Field(None, alias="mainPhoto")
    has_sizes: bool = Field(None, alias="hasSizes")
    metrics: Any = Field(None)
