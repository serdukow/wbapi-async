from typing import Any

from pydantic import Field

from ...types.base import BaseType


class MediaCampaignsNumberResponse(BaseType):
    """Media Campaigns Number"""

    all_: int | None = Field(None, alias="all")
    adverts: dict[str, Any] | None = Field(None)
