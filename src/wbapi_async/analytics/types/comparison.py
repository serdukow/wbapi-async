from pydantic import Field

from ...types.base import BaseType
from .conversions import Conversions
from .time_to_ready import TimeToReady
from .wb_club import WbClub


class Comparison(BaseType):
    open_count_dynamic: int = Field(alias="openCountDynamic")
    cart_count_dynamic: int = Field(alias="cartCountDynamic")
    order_count_dynamic: int = Field(alias="orderCountDynamic")
    order_sum_dynamic: int = Field(alias="orderSumDynamic")
    buyout_count_dynamic: int = Field(alias="buyoutCountDynamic")
    buyout_sum_dynamic: int = Field(alias="buyoutSumDynamic")
    cancel_count_dynamic: int = Field(alias="cancelCountDynamic")
    cancel_sum_dynamic: int = Field(alias="cancelSumDynamic")
    avg_orders_count_per_day_dynamic: int = Field(alias="avgOrdersCountPerDayDynamic")
    avg_price_dynamic: int = Field(alias="avgPriceDynamic")
    share_order_percent_dynamic: int = Field(alias="shareOrderPercentDynamic")
    add_to_wishlist_dynamic: int = Field(alias="addToWishlistDynamic")
    time_to_ready_dynamic: TimeToReady = Field(alias="timeToReadyDynamic")
    localization_percent_dynamic: int = Field(alias="localizationPercentDynamic")
    wb_club_dynamic: WbClub = Field(alias="wbClubDynamic")
    conversions: Conversions = Field(alias="conversions")
