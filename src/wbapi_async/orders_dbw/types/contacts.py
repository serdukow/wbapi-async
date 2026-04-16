from pydantic import Field

from ...types.base import BaseType


class Contacts(BaseType):
    """Courier contact information"""

    car_number: str | None = Field(None, alias="carNumber")
    full_name: str | None = Field(None, alias="fullName")
    phone: str | None = Field(None, alias="phone")
    p_time_from: str | None = Field(None, alias="pTimeFrom")
    p_time_to: str | None = Field(None, alias="pTimeTo")
