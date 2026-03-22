from pydantic import Field

from ...types.base import BaseType


class OrdersWithClientInformationItem(BaseType):
    """Orders with Client Information"""

    first_name: str | None = Field(None, alias="firstName")
    full_name: str | None = Field(None, alias="fullName")
    last_name: str | None = Field(None, alias="lastName")
    middle_name: str | None = Field(None, alias="middleName")
    order_id: int | None = Field(None, alias="orderID")
    phone: str | None = Field(None)
    phone_code: str | None = Field(None, alias="phoneCode")
