from enum import StrEnum


class AggregationLevel(StrEnum):
    """Aggregation Type. If not specified, the default is aggregation"""

    DAY = "day"
    WEEK = "week"
