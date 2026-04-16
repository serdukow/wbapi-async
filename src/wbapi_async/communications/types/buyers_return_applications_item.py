from pydantic import Field

from ...types.base import BaseType


class BuyersReturnApplicationsItem(BaseType):
    """Buyers Return Applications"""

    id_: str | None = Field(None, alias="id")
    claim_type: int | None = Field(None, alias="claim_type")
    status: int | None = Field(None, alias="status")
    status_ex: int | None = Field(None, alias="status_ex")
    nm_id: int | None = Field(None, alias="nm_id")
    user_comment: str | None = Field(None, alias="user_comment")
    wb_comment: str | None = Field(None, alias="wb_comment")
    dt: str | None = Field(None, alias="dt")
    imt_name: str | None = Field(None, alias="imt_name")
    order_dt: str | None = Field(None, alias="order_dt")
    dt_update: str | None = Field(None, alias="dt_update")
    photos: list[str] | None = Field(None, alias="photos")
    video_paths: list[str] | None = Field(None, alias="video_paths")
    actions: list[str] | None = Field(None, alias="actions")
    price: float | None = Field(None, alias="price")
    currency_code: str | None = Field(None, alias="currency_code")
    srid: str | None = Field(None, alias="srid")
    origin_id_info: str | None = Field(None, alias="origin_id_info")
    delivery_dt: str | None = Field(None, alias="delivery_dt")
