from pydantic import Field

from .base import BaseType


class ProcessedUploadDetailsItem(BaseType):
    """Processed Upload Details"""

    nm_id: int | None = Field(None, alias="nmID")
    vendor_code: str | None = Field(None, alias="vendorCode")
    size_id: int | None = Field(None, alias="sizeID")
    tech_size_name: str | None = Field(None, alias="techSizeName")
    price: int | None = Field(None)
    currency_iso_code4217: str | None = Field(None, alias="currencyIsoCode4217")
    discount: int | None = Field(None)
    club_discount: int | None = Field(None, alias="clubDiscount")
    status: int | None = Field(None)
    error_text: str | None = Field(None, alias="errorText")
