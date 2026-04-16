from pydantic import Field

from ...types.base import BaseType


class DataUpload(BaseType):
    """Request data"""

    promotion_id: int | None = Field(None, alias="promotionID")
    upload_now: bool | None = Field(None, alias="uploadNow")
    nomenclatures: list[int] | None = Field(None)
