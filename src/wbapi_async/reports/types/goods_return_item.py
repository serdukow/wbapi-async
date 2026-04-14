from pydantic import Field

from ...types.base import BaseType


class GoodsReturnItem(BaseType):
    """Goods return item"""

    barcode: str | None = Field(None, alias="barcode")
    brand: str | None = Field(None, alias="brand")
    completed_dt: str | None = Field(None, alias="completedDt")
    dst_office_address: str | None = Field(None, alias="dstOfficeAddress")
    dst_office_id: int | None = Field(None, alias="dstOfficeId")
    expired_dt: str | None = Field(None, alias="expiredDt")
    is_status_active: int | None = Field(None, alias="isStatusActive")
    nm_id: int | None = Field(None, alias="nmId")
    order_dt: str | None = Field(None, alias="orderDt")
    order_id: int | None = Field(None, alias="orderId")
    ready_to_return_dt: str | None = Field(None, alias="readyToReturnDt")
    reason: str | None = Field(None, alias="reason")
    return_type: str | None = Field(None, alias="returnType")
    shk_id: int | None = Field(None, alias="shkId")
    srid: str | None = Field(None, alias="srid")
    status: str | None = Field(None, alias="status")
    sticker_id: str | None = Field(None, alias="stickerId")
    subject_name: str | None = Field(None, alias="subjectName")
    tech_size: str | None = Field(None, alias="techSize")
