from pydantic import Field

from ...types.base import BaseType


class AssemblyOrdersStickersItem(BaseType):
    """Get Assembly Orders Stickers"""

    order_id: int | None = Field(None, alias="orderId")
    part_a: int | None = Field(None, alias="partA")
    part_b: int | None = Field(None, alias="partB")
    barcode: str | None = Field(None)
    file: str | None = Field(None)
