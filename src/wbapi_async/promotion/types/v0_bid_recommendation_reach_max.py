from pydantic import Field

from ...types.base import BaseType


class V0BidRecommendationReachMax(BaseType):
    """Max reach: 76–100%"""

    bid_kopecks: int | None = Field(None, alias="bidKopecks")
    bid_kopecks_min: int | None = Field(None, alias="bidKopecksMin")
