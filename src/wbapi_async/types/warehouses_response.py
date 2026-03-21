from pydantic import Field

from .base import BaseType


class WarehousesResponse(BaseType):
    """Get Warehouses"""

    name: str | None = Field(None)
    office_id: int | None = Field(None, alias="officeId")
    id: int | None = Field(None)
    cargo_type: int | None = Field(None, alias="cargoType")
    delivery_type: int | None = Field(None, alias="deliveryType")
    is_deleting: bool | None = Field(None, alias="isDeleting")
    is_processing: bool | None = Field(None, alias="isProcessing")
