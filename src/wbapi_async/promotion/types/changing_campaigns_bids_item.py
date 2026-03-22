from typing import Any

from pydantic import Field

from ...types.base import BaseType


class ChangingCampaignsBidsItem(BaseType):
    """Changing Campaigns Bids"""

    advert_id: int = Field()
    nm_bids: list[dict[str, Any]] = Field()
