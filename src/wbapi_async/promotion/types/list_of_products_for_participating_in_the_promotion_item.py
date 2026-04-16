from pydantic import Field

from ...types.base import BaseType


class ListOfProductsForParticipatingInThePromotionItem(BaseType):
    """List of Products for Participating in the Promotion"""

    id_: int | None = Field(None, alias="id")
    in_action: bool | None = Field(None, alias="inAction")
    price: float | None = Field(None, alias="price")
    currency_code: str | None = Field(None, alias="currencyCode")
    plan_price: float | None = Field(None, alias="planPrice")
    discount: int | None = Field(None, alias="discount")
    plan_discount: int | None = Field(None, alias="planDiscount")
