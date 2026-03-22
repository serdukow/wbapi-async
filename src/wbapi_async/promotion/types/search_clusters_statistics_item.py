from typing import Any

from pydantic import Field

from ...types.base import BaseType


class SearchClustersStatisticsItem(BaseType):
    """Search Clusters Statistics"""

    advert_id: int = Field()
    nm_id: int = Field()
    stats: list[Any] | None = Field(None)
