from typing import Any

from pydantic import Field

from .base import BaseType


class CampaignsListsItem(BaseType):
    """Campaigns Lists"""

    type: int | None = Field(None)
    status: int | None = Field(None)
    count: int | None = Field(None)
    advert_list: list[dict[str, Any]] | None = Field(None)
