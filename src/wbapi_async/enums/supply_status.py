from enum import IntEnum


class SupplyStatus(IntEnum):
    NOT_PLANNED = 1
    PLANNED = 2
    UNLOADING_ALLOWED = 3
    ACCEPTING = 4
    ACCEPTED = 5
    UNLOADED_AT_GATE = 6
