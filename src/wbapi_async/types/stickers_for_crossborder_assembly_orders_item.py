from pydantic import Field

from .base import BaseType


class StickersForCrossborderAssemblyOrdersItem(BaseType):
    """Get Stickers for Cross-Border Assembly Orders"""

    file: str | None = Field(None)
    order_id: int | None = Field(None, alias="orderId")
    parcel_id: str | None = Field(None, alias="parcelId")
