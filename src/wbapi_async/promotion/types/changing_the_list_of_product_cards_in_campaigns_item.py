from pydantic import Field

from ...types.base import BaseType
from .nms_2 import Nms2


class ChangingTheListOfProductCardsInCampaignsItem(BaseType):
    """Changing the List of Product Cards in Campaigns"""

    advert_id: int = Field(alias="advert_id")
    nms: Nms2 = Field(alias="nms")
