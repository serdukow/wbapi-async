from pydantic import Field

from ...types.base import BaseType


class StickersForAssemblyOrdersWithDeliveryToPickupPointItem(BaseType):
    """Get Stickers for Assembly Orders with Delivery to Pickup Point"""

    order_id: int = Field(alias="orderId")
    part_a: str = Field(alias="partA")
    part_b: str = Field(alias="partB")
    barcode: str = Field()
    file: str = Field()
