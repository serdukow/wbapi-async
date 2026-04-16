from pydantic import Field

from ...types.base import BaseType
from .v0_bid_recommendation_reach_max import V0BidRecommendationReachMax
from .v0_bid_recommendation_reach_medium import V0BidRecommendationReachMedium
from .v0_bid_recommendation_reach_min import V0BidRecommendationReachMin


class RecommendedBidsForItemsAndSearchClustersItem(BaseType):
    """Recommended bids for items and search clusters"""

    norm_query: str | None = Field(None, alias="normQuery")
    reach_max: V0BidRecommendationReachMax | None = Field(None, alias="reachMax")
    reach_medium: V0BidRecommendationReachMedium | None = Field(None, alias="reachMedium")
    reach_min: V0BidRecommendationReachMin | None = Field(None, alias="reachMin")
