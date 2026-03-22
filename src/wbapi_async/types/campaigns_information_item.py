from typing import Any

from pydantic import Field

from .base import BaseType


class CampaignsInformationItem(BaseType):
    """Campaigns Information"""

    bid_type: str = Field(None)
    id: int = Field(None)
    nm_settings: list[Any] = Field(None)
    settings: dict[str, Any] = Field(None)
    status: int = Field(None)
    timestamps: dict[str, Any] = Field(None)
