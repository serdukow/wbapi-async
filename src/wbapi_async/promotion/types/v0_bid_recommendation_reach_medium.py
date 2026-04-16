from pydantic import Field

from ...types.base import BaseType


class V0BidRecommendationReachMedium(BaseType):
    """Medium reach: 61-75% coverage"""

    bid_kopecks: int | None = Field(None, alias="bidKopecks")
    bid_kopecks_min: int | None = Field(None, alias="bidKopecksMin")
