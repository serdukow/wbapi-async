from pydantic import Field

from .base import BaseType


class ReportItem(BaseType):
    """Get Report"""

    barcode: str | None = Field(None)
    brand: str | None = Field(None)
    completed_dt: str | None = Field(None, alias="completedDt")
    dst_office_address: str | None = Field(None, alias="dstOfficeAddress")
    dst_office_id: int | None = Field(None, alias="dstOfficeId")
    expired_dt: str | None = Field(None, alias="expiredDt")
    is_status_active: int | None = Field(None, alias="isStatusActive")
    nm_id: int | None = Field(None, alias="nmId")
    order_dt: str | None = Field(None, alias="orderDt")
    order_id: int | None = Field(None, alias="orderId")
    ready_to_return_dt: str | None = Field(None, alias="readyToReturnDt")
    reason: str | None = Field(None)
    return_type: str | None = Field(None, alias="returnType")
    shk_id: int | None = Field(None, alias="shkId")
    srid: str | None = Field(None)
    status: str | None = Field(None)
    sticker_id: str | None = Field(None, alias="stickerId")
    subject_name: str | None = Field(None, alias="subjectName")
    tech_size: str | None = Field(None, alias="techSize")
