from pydantic import Field

from ...types.base import BaseType


class Conversions(BaseType):
    add_to_cart_percent: int = Field(alias="addToCartPercent")
    cart_to_order_percent: int = Field(alias="cartToOrderPercent")
    buyout_percent: int = Field(alias="buyoutPercent")
