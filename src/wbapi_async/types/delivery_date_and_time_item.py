from pydantic import Field

from .base import BaseType


class DeliveryDateAndTimeItem(BaseType):
    """Delivery Date and Time"""

    d_time_from: str | None = Field(None, alias="dTimeFrom")
    d_time_to: str | None = Field(None, alias="dTimeTo")
    d_time_from_old: str | None = Field(None, alias="dTimeFromOld")
    d_time_to_old: str | None = Field(None, alias="dTimeToOld")
    d_date_old: str | None = Field(None, alias="dDateOld")
    d_date: str | None = Field(None, alias="dDate")
    id: int | None = Field(None)
