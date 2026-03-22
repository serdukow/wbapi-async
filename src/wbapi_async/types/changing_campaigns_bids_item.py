from typing import Any

from pydantic import Field

from .base import BaseType


class ChangingCampaignsBidsItem(BaseType):
    """Changing Campaigns Bids"""

    advert_id: int = Field(None)
    nm_bids: list[dict[str, Any]] = Field(None)
