from pydantic import Field

from .base import BaseType


class InventoryItem(BaseType):
    """Get Inventory"""

    chrt_id: int | None = Field(None, alias="chrtId")
    amount: int | None = Field(None)
