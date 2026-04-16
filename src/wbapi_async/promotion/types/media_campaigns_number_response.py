from pydantic import Field

from ...types.base import BaseType
from .adverts import Adverts


class MediaCampaignsNumberResponse(BaseType):
    """Media Campaigns Number"""

    all_: int | None = Field(None, alias="all")
    adverts: Adverts | None = Field(None)
