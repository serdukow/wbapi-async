from pydantic import Field

from ...types.base import BaseType


class WarehousesResponse(BaseType):
    """Get Warehouses"""

    name: str | None = Field(None, alias="name")
    office_id: int | None = Field(None, alias="officeId")
    id_: int | None = Field(None, alias="id")
    cargo_type: int | None = Field(None, alias="cargoType")
    delivery_type: int | None = Field(None, alias="deliveryType")
    is_deleting: bool | None = Field(None, alias="isDeleting")
    is_processing: bool | None = Field(None, alias="isProcessing")
