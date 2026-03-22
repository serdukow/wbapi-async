from typing import Any

from pydantic import Field

from .base import BaseType


class SupplyPackageResponse(BaseType):
    """Supply Package"""

    package_code: str | None = Field(None, alias="packageCode")
    quantity: int | None = Field(None)
    barcodes: list[Any] | None = Field(None)
