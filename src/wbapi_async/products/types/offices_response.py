from pydantic import Field

from ...types.base import BaseType


class OfficesResponse(BaseType):
    """Get Offices"""

    address: str | None = Field(None)
    name: str | None = Field(None)
    city: str | None = Field(None)
    id_: int | None = Field(None, alias="id")
    longitude: float | None = Field(None)
    latitude: float | None = Field(None)
    cargo_type: int | None = Field(None, alias="cargoType")
    delivery_type: int | None = Field(None, alias="deliveryType")
    federal_district: str | None = Field(None, alias="federalDistrict")
    selected: bool | None = Field(None)
