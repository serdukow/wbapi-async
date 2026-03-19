from enum import StrEnum


class ProductDataOrderField(StrEnum):
    ORDERS_COUNT = "ordersCount"
    ORDERS_SUM = "ordersSum"
    AVG_ORDERS = "avgOrders"
    BUYOUT_COUNT = "buyoutCount"
    BUYOUT_SUM = "buyoutSum"
    BUYOUT_PERCENT = "buyoutPercent"
    STOCK_COUNT = "stockCount"
    STOCK_SUM = "stockSum"
    SALE_RATE = "saleRate"
    AVG_STOCK_TURNOVER = "avgStockTurnover"
    TO_CLIENT_COUNT = "toClientCount"
    FROM_CLIENT_COUNT = "fromClientCount"
    MIN_PRICE = "minPrice"
    MAX_PRICE = "maxPrice"
    OFFICE_MISSING_TIME = "officeMissingTime"
    LOST_ORDERS_COUNT = "lostOrdersCount"
    LOST_ORDERS_SUM = "lostOrdersSum"
    LOST_BUYOUTS_COUNT = "lostBuyoutsCount"
    LOST_BUYOUTS_SUM = "lostBuyoutsSum"
