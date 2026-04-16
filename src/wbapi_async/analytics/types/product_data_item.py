from pydantic import Field

from ...types.base import BaseType
from .metrics import Metrics


class ProductDataItem(BaseType):
    """Product Data"""

    nm_id: int = Field(alias="nmID")
    is_deleted: bool = Field(alias="isDeleted")
    subject_name: str = Field(alias="subjectName")
    name: str = Field(alias="name")
    vendor_code: str = Field(alias="vendorCode")
    brand_name: str = Field(alias="brandName")
    main_photo: str = Field(alias="mainPhoto")
    has_sizes: bool = Field(alias="hasSizes")
    metrics: Metrics = Field(alias="metrics")
