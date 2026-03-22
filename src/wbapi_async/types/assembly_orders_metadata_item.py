from pydantic import Field

from .base import BaseType


class AssemblyOrdersMetadataItem(BaseType):
    """Get Assembly Orders Metadata"""

    error: str = Field(None)
    gtin: str | None = Field(None)
    imei: str | None = Field(None)
    order_id: int = Field(None, alias="orderId")
    sgtin: list[str] | None = Field(None)
    uin: str | None = Field(None)
