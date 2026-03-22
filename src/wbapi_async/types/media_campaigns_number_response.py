from typing import Any

from pydantic import Field

from .base import BaseType


class MediaCampaignsNumberResponse(BaseType):
    """Media Campaigns Number"""

    all: int | None = Field(None)
    adverts: dict[str, Any] | None = Field(None)
