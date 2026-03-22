from enum import StrEnum


class TopOrderBy(StrEnum):
    """Filtering by the search queries that brought the most:"""

    OPENCARD = "openCard"
    ADDTOCART = "addToCart"
    OPENTOCART = "openToCart"
    ORDERS = "orders"
    CARTTOORDER = "cartToOrder"
