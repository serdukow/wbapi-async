from pydantic import Field

from ...types.base import BaseType
from .conversions import Conversions
from .period import Period
from .time_to_ready import TimeToReady
from .wb_club import WbClub


class Past(BaseType):
    period: Period = Field()
    open_count: int = Field(alias="openCount")
    cart_count: int = Field(alias="cartCount")
    order_count: int = Field(alias="orderCount")
    order_sum: int = Field(alias="orderSum")
    buyout_count: int = Field(alias="buyoutCount")
    buyout_sum: int = Field(alias="buyoutSum")
    cancel_count: int = Field(alias="cancelCount")
    cancel_sum: int = Field(alias="cancelSum")
    avg_price: int = Field(alias="avgPrice")
    avg_orders_count_per_day: float = Field(alias="avgOrdersCountPerDay")
    share_order_percent: float = Field(alias="shareOrderPercent")
    add_to_wishlist: int = Field(alias="addToWishlist")
    time_to_ready: TimeToReady = Field(alias="timeToReady")
    localization_percent: int = Field(alias="localizationPercent")
    wb_club: WbClub = Field(alias="wbClub")
    conversions: Conversions = Field()
