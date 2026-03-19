from pydantic import Field

from ..enums.product_data_availability import ProductDataAvailability
from .base import BaseType


class DaysHours(BaseType):
    days: int | None = Field(None, alias="days")
    hours: int | None = Field(None, alias="hours")


class AvgOrdersByMonth(BaseType):
    start: str | None = Field(None, alias="start")
    end: str | None = Field(None, alias="end")
    value: float | None = Field(None, alias="value")


class CurrentPrice(BaseType):
    min_price: float | None = Field(None, alias="minPrice")
    max_price: float | None = Field(None, alias="maxPrice")


class ProductMetrics(BaseType):
    orders_count: int | None = Field(None, alias="ordersCount")
    orders_sum: float | None = Field(None, alias="ordersSum")
    avg_orders: float | None = Field(None, alias="avgOrders")
    avg_orders_by_month: list[AvgOrdersByMonth] | None = Field(None, alias="avgOrdersByMonth")
    buyout_count: int | None = Field(None, alias="buyoutCount")
    buyout_sum: float | None = Field(None, alias="buyoutSum")
    buyout_percent: float | None = Field(None, alias="buyoutPercent")
    stock_count: int | None = Field(None, alias="stockCount")
    stock_sum: float | None = Field(None, alias="stockSum")
    sale_rate: DaysHours | None = Field(None, alias="saleRate")
    avg_stock_turnover: DaysHours | None = Field(None, alias="avgStockTurnover")
    to_client_count: int | None = Field(None, alias="toClientCount")
    from_client_count: int | None = Field(None, alias="fromClientCount")
    office_missing_time: DaysHours | None = Field(None, alias="officeMissingTime")
    lost_orders_count: float | None = Field(None, alias="lostOrdersCount")
    lost_orders_sum: float | None = Field(None, alias="lostOrdersSum")
    lost_buyouts_count: float | None = Field(None, alias="lostBuyoutsCount")
    lost_buyouts_sum: float | None = Field(None, alias="lostBuyoutsSum")
    current_price: CurrentPrice | None = Field(None, alias="currentPrice")
    availability: ProductDataAvailability | None = Field(None, alias="availability")


class ProductDataItem(BaseType):
    nm_id: int | None = Field(None, alias="nmID")
    is_deleted: bool | None = Field(None, alias="isDeleted")
    subject_name: str | None = Field(None, alias="subjectName")
    name: str | None = Field(None, alias="name")
    vendor_code: str | None = Field(None, alias="vendorCode")
    brand_name: str | None = Field(None, alias="brandName")
    main_photo: str | None = Field(None, alias="mainPhoto")
    has_sizes: bool | None = Field(None, alias="hasSizes")
    metrics: ProductMetrics | None = Field(None, alias="metrics")
