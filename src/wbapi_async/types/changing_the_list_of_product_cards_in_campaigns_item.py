from typing import Any

from pydantic import Field

from .base import BaseType


class ChangingTheListOfProductCardsInCampaignsItem(BaseType):
    """Changing the List of Product Cards in Campaigns"""

    advert_id: int = Field(None)
    nms: dict[str, Any] = Field(None)
