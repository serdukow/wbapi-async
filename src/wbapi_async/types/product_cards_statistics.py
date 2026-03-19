from pydantic import Field

from .base import BaseType


class Tag(BaseType):
    id: int | None = Field(None, alias="id")
    name: str | None = Field(None, alias="name")


class Stocks(BaseType):
    wb: int | None = Field(None, alias="wb")
    mp: int | None = Field(None, alias="mp")
    balance_sum: float | None = Field(None, alias="balanceSum")


class ProductInfo(BaseType):
    nm_id: int | None = Field(None, alias="nmId")
    title: str | None = Field(None, alias="title")
    vendor_code: str | None = Field(None, alias="vendorCode")
    brand_name: str | None = Field(None, alias="brandName")
    subject_id: int | None = Field(None, alias="subjectId")
    subject_name: str | None = Field(None, alias="subjectName")
    tags: list[Tag] | None = Field(None, alias="tags")
    product_rating: float | None = Field(None, alias="productRating")
    feedback_rating: float | None = Field(None, alias="feedbackRating")
    stocks: Stocks | None = Field(None, alias="stocks")


class DaysHoursMinutes(BaseType):
    days: int | None = Field(None, alias="days")
    hours: int | None = Field(None, alias="hours")
    mins: int | None = Field(None, alias="mins")


class WbClubStats(BaseType):
    order_count: int | None = Field(None, alias="orderCount")
    order_sum: float | None = Field(None, alias="orderSum")
    buyout_sum: float | None = Field(None, alias="buyoutSum")
    buyout_count: int | None = Field(None, alias="buyoutCount")
    cancel_sum: float | None = Field(None, alias="cancelSum")
    cancel_count: int | None = Field(None, alias="cancelCount")
    avg_price: float | None = Field(None, alias="avgPrice")
    buyout_percent: float | None = Field(None, alias="buyoutPercent")
    avg_order_count_per_day: float | None = Field(None, alias="avgOrderCountPerDay")


class Conversions(BaseType):
    add_to_cart_percent: float | None = Field(None, alias="addToCartPercent")
    cart_to_order_percent: float | None = Field(None, alias="cartToOrderPercent")
    buyout_percent: float | None = Field(None, alias="buyoutPercent")


class PeriodStats(BaseType):
    period: dict | None = Field(None, alias="period")
    open_count: int | None = Field(None, alias="openCount")
    cart_count: int | None = Field(None, alias="cartCount")
    order_count: int | None = Field(None, alias="orderCount")
    order_sum: float | None = Field(None, alias="orderSum")
    buyout_count: int | None = Field(None, alias="buyoutCount")
    buyout_sum: float | None = Field(None, alias="buyoutSum")
    cancel_count: int | None = Field(None, alias="cancelCount")
    cancel_sum: float | None = Field(None, alias="cancelSum")
    avg_price: float | None = Field(None, alias="avgPrice")
    avg_orders_count_per_day: float | None = Field(None, alias="avgOrdersCountPerDay")
    share_order_percent: float | None = Field(None, alias="shareOrderPercent")
    add_to_wishlist: int | None = Field(None, alias="addToWishlist")
    time_to_ready: DaysHoursMinutes | None = Field(None, alias="timeToReady")
    localization_percent: float | None = Field(None, alias="localizationPercent")
    wb_club: WbClubStats | None = Field(None, alias="wbClub")
    conversions: Conversions | None = Field(None, alias="conversions")


class ComparisonStats(BaseType):
    open_count_dynamic: float | None = Field(None, alias="openCountDynamic")
    cart_count_dynamic: float | None = Field(None, alias="cartCountDynamic")
    order_count_dynamic: float | None = Field(None, alias="orderCountDynamic")
    order_sum_dynamic: float | None = Field(None, alias="orderSumDynamic")
    buyout_count_dynamic: float | None = Field(None, alias="buyoutCountDynamic")
    buyout_sum_dynamic: float | None = Field(None, alias="buyoutSumDynamic")
    cancel_count_dynamic: float | None = Field(None, alias="cancelCountDynamic")
    cancel_sum_dynamic: float | None = Field(None, alias="cancelSumDynamic")
    avg_orders_count_per_day_dynamic: float | None = Field(
        None, alias="avgOrdersCountPerDayDynamic"
    )
    avg_price_dynamic: float | None = Field(None, alias="avgPriceDynamic")
    share_order_percent_dynamic: float | None = Field(None, alias="shareOrderPercentDynamic")
    add_to_wishlist_dynamic: float | None = Field(None, alias="addToWishlistDynamic")
    time_to_ready_dynamic: DaysHoursMinutes | None = Field(None, alias="timeToReadyDynamic")
    localization_percent_dynamic: float | None = Field(None, alias="localizationPercentDynamic")
    wb_club_dynamic: WbClubStats | None = Field(None, alias="wbClubDynamic")
    conversions: Conversions | None = Field(None, alias="conversions")


class ProductStatistic(BaseType):
    selected: PeriodStats | None = Field(None, alias="selected")
    past: PeriodStats | None = Field(None, alias="past")
    comparison: ComparisonStats | None = Field(None, alias="comparison")


class ProductCardStatistics(BaseType):
    product: ProductInfo | None = Field(None, alias="product")
    statistic: ProductStatistic | None = Field(None, alias="statistic")
