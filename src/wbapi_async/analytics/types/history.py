from pydantic import Field

from ...types.base import BaseType


class History(BaseType):
    date: str = Field(alias="date")
    open_count: int = Field(alias="openCount")
    cart_count: int = Field(alias="cartCount")
    order_count: int = Field(alias="orderCount")
    order_sum: int = Field(alias="orderSum")
    buyout_count: int = Field(alias="buyoutCount")
    buyout_sum: int = Field(alias="buyoutSum")
    buyout_percent: int = Field(alias="buyoutPercent")
    add_to_cart_conversion: int = Field(alias="addToCartConversion")
    cart_to_order_conversion: int = Field(alias="cartToOrderConversion")
    add_to_wishlist_count: int = Field(alias="addToWishlistCount")
