from pydantic import Field

from ...types.base import BaseType


class SupplierTaskMetadataBuffer(BaseType):
    """Response data"""

    upload_id: int | None = Field(None, alias="uploadID")
    status: int | None = Field(None)
    upload_date: str | None = Field(None, alias="uploadDate")
    activation_date: str | None = Field(None, alias="activationDate")
    over_all_goods_number: int | None = Field(None, alias="overAllGoodsNumber")
    success_goods_number: int | None = Field(None, alias="successGoodsNumber")
