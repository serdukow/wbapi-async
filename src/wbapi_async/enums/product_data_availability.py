from enum import StrEnum


class ProductDataAvailability(StrEnum):
    DEFICIENT = "deficient"
    ACTUAL = "actual"
    BALANCED = "balanced"
    NON_ACTUAL = "nonActual"
    NON_LIQUID = "nonLiquid"
    INVALID_DATA = "invalidData"
