from pydantic import Field

from ...types.base import BaseType


class BuyersReturnApplicationsItem(BaseType):
    """Buyers Return Applications"""

    id: str | None = Field(None)
    claim_type: int | None = Field(None)
    status: int | None = Field(None)
    status_ex: int | None = Field(None)
    nm_id: int | None = Field(None)
    user_comment: str | None = Field(None)
    wb_comment: str | None = Field(None)
    dt: str | None = Field(None)
    imt_name: str | None = Field(None)
    order_dt: str | None = Field(None)
    dt_update: str | None = Field(None)
    photos: list[str] | None = Field(None)
    video_paths: list[str] | None = Field(None)
    actions: list[str] | None = Field(None)
    price: float | None = Field(None)
    currency_code: str | None = Field(None)
    srid: str | None = Field(None)
    origin_id_info: str | None = Field(None)
    delivery_dt: str | None = Field(None)
