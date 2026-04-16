from pydantic import Field

from ...types.base import BaseType


class Address(BaseType):
    """Exact buyer's address for delivery, if applicable. Some of the fields may be empty due to the spe..."""

    full_address: str | None = Field(None, alias="fullAddress")
    longitude: float | None = Field(None, alias="longitude")
    latitude: float | None = Field(None, alias="latitude")
