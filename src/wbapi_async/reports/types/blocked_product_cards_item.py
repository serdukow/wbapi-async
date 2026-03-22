from pydantic import Field

from ...types.base import BaseType


class BlockedProductCardsItem(BaseType):
    """Blocked Product Cards"""

    brand: str | None = Field(None)
    nm_id: int | None = Field(None, alias="nmId")
    title: str | None = Field(None)
    vendor_code: str | None = Field(None, alias="vendorCode")
    reason: str | None = Field(None)
