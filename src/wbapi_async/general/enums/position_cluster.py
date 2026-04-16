from enum import StrEnum


class PositionCluster(StrEnum):
    """Which average search position of products to display in the report:"""

    ALL = "all"
    FIRSTHUNDRED = "firstHundred"
    SECONDHUNDRED = "secondHundred"
    BELOW = "below"
