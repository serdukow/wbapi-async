from pydantic import Field

from ...types.base import BaseType
from .nm_bids_item import NmBidsItem


class ChangingCampaignsBidsItem(BaseType):
    """Changing Campaigns Bids"""

    advert_id: int = Field()
    nm_bids: list[NmBidsItem] = Field()
