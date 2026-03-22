from pydantic import Field

from .base import BaseType


class ListOfSearchClustersBidsItem(BaseType):
    """List of Search Clusters Bids"""

    advert_id: int = Field(None)
    nm_id: int = Field(None)
    norm_query: str = Field(None)
    bid: int = Field(None)
