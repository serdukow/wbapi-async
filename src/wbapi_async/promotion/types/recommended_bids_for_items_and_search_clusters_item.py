from typing import Any

from pydantic import Field

from ...types.base import BaseType


class RecommendedBidsForItemsAndSearchClustersItem(BaseType):
    """Recommended bids for items and search clusters"""

    norm_query: str | None = Field(None, alias="normQuery")
    reach_max: dict[str, Any] | None = Field(None, alias="reachMax")
    reach_medium: dict[str, Any] | None = Field(None, alias="reachMedium")
    reach_min: dict[str, Any] | None = Field(None, alias="reachMin")
