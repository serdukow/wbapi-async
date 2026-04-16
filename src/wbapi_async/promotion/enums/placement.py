from enum import StrEnum


class Placement(StrEnum):
    """Placement:"""

    SEARCH = "search"
    RECOMMENDATIONS = "recommendations"
    COMBINED = "combined"
