from pydantic import Field

from ...types.base import BaseType


class PassesResponse(BaseType):
    """Get Passes"""

    first_name: str | None = Field(None, alias="firstName")
    date_end: str | None = Field(None, alias="dateEnd")
    last_name: str | None = Field(None, alias="lastName")
    car_model: str | None = Field(None, alias="carModel")
    car_number: str | None = Field(None, alias="carNumber")
    office_name: str | None = Field(None, alias="officeName")
    office_address: str | None = Field(None, alias="officeAddress")
    office_id: int | None = Field(None, alias="officeId")
    id: int | None = Field(None)
