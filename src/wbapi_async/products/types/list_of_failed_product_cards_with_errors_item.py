from typing import Any

from pydantic import Field

from ...types.base import BaseType


class ListOfFailedProductCardsWithErrorsItem(BaseType):
    """List of Failed Product Cards with Errors"""

    batch_uuid: str = Field(alias="batchUUID")
    subjects: dict[str, Any] = Field(alias="subjects")
    brands: dict[str, Any] = Field(alias="brands")
    vendor_codes: list[str] = Field(alias="vendorCodes")
    errors: dict[str, Any] = Field(alias="errors")
