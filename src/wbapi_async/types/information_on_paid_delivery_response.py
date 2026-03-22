from pydantic import Field

from .base import BaseType


class InformationOnPaidDeliveryResponse(BaseType):
    """Get Information on Paid Delivery"""

    group_id: str | None = Field(None, alias="groupID")
    delivery_cost: int | None = Field(None, alias="deliveryCost")
    converted_delivery_cost: int | None = Field(None, alias="convertedDeliveryCost")
    currency_code: int | None = Field(None, alias="currencyCode")
    converted_currency_code: int | None = Field(None, alias="convertedCurrencyCode")
