from pydantic import Field

from .base import BaseType


class TheSupplyBoxQrCodeStickersItem(BaseType):
    """Get the Supply Box QR Code Stickers"""

    barcode: str | None = Field(None)
    file: str | None = Field(None)
