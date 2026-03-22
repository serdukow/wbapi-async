from pydantic import Field

from ...types.base import BaseType


class ListOfSearchClustersBidsItem(BaseType):
    """List of Search Clusters Bids"""

    advert_id: int = Field()
    nm_id: int = Field()
    norm_query: str = Field()
    bid: int = Field()
