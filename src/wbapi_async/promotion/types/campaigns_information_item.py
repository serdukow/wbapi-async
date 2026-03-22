from typing import Any

from pydantic import Field

from ...types.base import BaseType


class CampaignsInformationItem(BaseType):
    """Campaigns Information"""

    bid_type: str = Field()
    id: int = Field()
    nm_settings: list[Any] = Field()
    settings: dict[str, Any] = Field()
    status: int = Field()
    timestamps: dict[str, Any] = Field()
