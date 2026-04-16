from pydantic import Field

from ...types.base import BaseType


class BuyerInformationItem(BaseType):
    """Buyer Information"""

    replacement_phone: str | None = Field(None, alias="replacementPhone")
    phone: str | None = Field(None, alias="phone")
    first_name: str | None = Field(None, alias="firstName")
    full_name: str | None = Field(None, alias="fullName")
    additional_phones: list[str] | None = Field(None, alias="additionalPhones")
    additional_phone_codes: list[int] | None = Field(None, alias="additionalPhoneCodes")
    order_id: int | None = Field(None, alias="orderId")
    phone_code: int | None = Field(None, alias="phoneCode")
