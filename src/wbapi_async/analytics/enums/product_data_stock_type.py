from enum import StrEnum


class ProductDataStockType(StrEnum):
    """Type of products storage warehouse"""

    ALL = ""
    WB = "wb"
    MP = "mp"
