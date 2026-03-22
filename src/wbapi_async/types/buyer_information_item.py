from pydantic import Field

from .base import BaseType


class BuyerInformationItem(BaseType):
    """Buyer Information"""

    phone: str | None = Field(None)
    first_name: str | None = Field(None, alias="firstName")
    order_id: int | None = Field(None, alias="orderID")
    phone_code: int | None = Field(None, alias="phoneCode")
