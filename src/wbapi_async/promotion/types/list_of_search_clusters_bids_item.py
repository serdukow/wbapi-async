from pydantic import Field

from ...types.base import BaseType


class ListOfSearchClustersBidsItem(BaseType):
    """List of Search Clusters Bids"""

    advert_id: int = Field(alias="advert_id")
    nm_id: int = Field(alias="nm_id")
    norm_query: str = Field(alias="norm_query")
    bid: int = Field(alias="bid")
