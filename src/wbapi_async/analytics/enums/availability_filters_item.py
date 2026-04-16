from enum import StrEnum


class AvailabilityFiltersItem(StrEnum):
    DEFICIENT = "deficient"
    ACTUAL = "actual"
    BALANCED = "balanced"
    NONACTUAL = "nonActual"
    NONLIQUID = "nonLiquid"
    INVALIDDATA = "invalidData"
