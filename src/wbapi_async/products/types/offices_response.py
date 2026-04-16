from pydantic import Field

from ...types.base import BaseType


class OfficesResponse(BaseType):
    """Get Offices"""

    address: str | None = Field(None, alias="address")
    name: str | None = Field(None, alias="name")
    city: str | None = Field(None, alias="city")
    id_: int | None = Field(None, alias="id")
    longitude: float | None = Field(None, alias="longitude")
    latitude: float | None = Field(None, alias="latitude")
    cargo_type: int | None = Field(None, alias="cargoType")
    delivery_type: int | None = Field(None, alias="deliveryType")
    federal_district: str | None = Field(None, alias="federalDistrict")
    selected: bool | None = Field(None, alias="selected")
