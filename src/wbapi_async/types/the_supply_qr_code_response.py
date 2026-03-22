from pydantic import Field

from .base import BaseType


class TheSupplyQrCodeResponse(BaseType):
    """Get the Supply QR Code"""

    barcode: str | None = Field(None)
    file: str | None = Field(None)
