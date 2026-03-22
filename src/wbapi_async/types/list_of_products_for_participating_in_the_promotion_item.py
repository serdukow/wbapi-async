from pydantic import Field

from .base import BaseType


class ListOfProductsForParticipatingInThePromotionItem(BaseType):
    """List of Products for Participating in the Promotion"""

    id: int | None = Field(None)
    in_action: bool | None = Field(None, alias="inAction")
    price: float | None = Field(None)
    currency_code: str | None = Field(None, alias="currencyCode")
    plan_price: float | None = Field(None, alias="planPrice")
    discount: int | None = Field(None)
    plan_discount: int | None = Field(None, alias="planDiscount")
