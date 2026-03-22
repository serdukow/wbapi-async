from pydantic import Field

from .base import BaseType


class StickersForAssemblyOrdersWithDeliveryToPickupPointItem(BaseType):
    """Get Stickers for Assembly Orders with Delivery to Pickup Point"""

    order_id: int = Field(None, alias="orderId")
    part_a: str = Field(None, alias="partA")
    part_b: str = Field(None, alias="partB")
    barcode: str = Field(None)
    file: str = Field(None)
