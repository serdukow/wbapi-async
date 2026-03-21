from typing import Any

from pydantic import Field

from .base import BaseType


class ListOfFailedProductCardsWithErrorsItem(BaseType):
    """List of Failed Product Cards with Errors"""

    batch_uuid: str = Field(None, alias="batchUUID")
    subjects: dict[str, Any] = Field(None)
    brands: dict[str, Any] = Field(None)
    vendor_codes: list[str] = Field(None, alias="vendorCodes")
    errors: dict[str, Any] = Field(None)
