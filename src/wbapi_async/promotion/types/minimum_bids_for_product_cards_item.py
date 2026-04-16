from pydantic import Field

from ...types.base import BaseType
from .bids_item import BidsItem


class MinimumBidsForProductCardsItem(BaseType):
    """Minimum Bids for Product Cards"""

    bids: list[BidsItem] = Field(alias="bids")
    nm_id: int = Field(alias="nm_id")
