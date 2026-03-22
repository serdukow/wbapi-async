from typing import Any

from pydantic import Field

from ...types.base import BaseType


class ChangingTheListOfProductCardsInCampaignsItem(BaseType):
    """Changing the List of Product Cards in Campaigns"""

    advert_id: int = Field()
    nms: dict[str, Any] = Field()
