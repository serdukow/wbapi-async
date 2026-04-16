from pydantic import Field

from ...types.base import BaseType


class V0BidRecommendationReachMin(BaseType):
    """Minimum reach: 50-60%"""

    bid_kopecks: int | None = Field(None, alias="bidKopecks")
    bid_kopecks_min: int | None = Field(None, alias="bidKopecksMin")
