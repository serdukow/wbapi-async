from pydantic import Field

from ...types.base import BaseType


class OrdersStickersItem(BaseType):
    """Get Orders Stickers"""

    order_id: int | None = Field(None, alias="orderId")
    part_a: str | None = Field(None, alias="partA")
    part_b: str | None = Field(None, alias="partB")
    barcode: str | None = Field(None)
    file: str | None = Field(None)
