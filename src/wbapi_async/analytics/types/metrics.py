from pydantic import Field

from ...types.base import BaseType
from .float_graph_by_period_item import FloatGraphByPeriodItem
from .sale_rate import SaleRate


class Metrics(BaseType):
    """Group metrics"""

    orders_count: int = Field(alias="ordersCount")
    orders_sum: int = Field(alias="ordersSum")
    avg_orders: float = Field(alias="avgOrders")
    avg_orders_by_month: list[FloatGraphByPeriodItem] = Field(alias="avgOrdersByMonth")
    buyout_count: int = Field(alias="buyoutCount")
    buyout_sum: int = Field(alias="buyoutSum")
    buyout_percent: int = Field(alias="buyoutPercent")
    stock_count: int = Field(alias="stockCount")
    stock_sum: int = Field(alias="stockSum")
    sale_rate: SaleRate = Field(alias="saleRate")
    avg_stock_turnover: SaleRate = Field(alias="avgStockTurnover")
    to_client_count: int = Field(alias="toClientCount")
    from_client_count: int = Field(alias="fromClientCount")
    office_missing_time: SaleRate = Field(alias="officeMissingTime")
    lost_orders_count: float = Field(alias="lostOrdersCount")
    lost_orders_sum: float = Field(alias="lostOrdersSum")
    lost_buyouts_count: float = Field(alias="lostBuyoutsCount")
    lost_buyouts_sum: float = Field(alias="lostBuyoutsSum")
