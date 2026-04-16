from pydantic import Field

from ...types.base import BaseType


class StickersForCrossborderAssemblyOrdersItem(BaseType):
    """Get Stickers for Cross-Border Assembly Orders"""

    order_id: int | None = Field(None, alias="orderId")
    status: str | None = Field(None)
    parcel_id: str | None = Field(None, alias="parcelId")
    file: str | None = Field(None)
    part_a: str | None = Field(None, alias="partA")
    part_b: str | None = Field(None, alias="partB")
    barcode: str | None = Field(None)
