from pydantic import Field

from ...types.base import BaseType


class TheSupplyQrCodeResponse(BaseType):
    """Get the Supply QR Code"""

    barcode: str | None = Field(None, alias="barcode")
    file: str | None = Field(None, alias="file")
