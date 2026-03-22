from typing import Any

from pydantic import Field

from .base import BaseType


class SearchClustersStatisticsItem(BaseType):
    """Search Clusters Statistics"""

    advert_id: int = Field(None)
    nm_id: int = Field(None)
    stats: list[Any] | None = Field(None)
