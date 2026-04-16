from pydantic import Field

from ...types.base import BaseType
from .advert_nms_settings import AdvertNmsSettings
from .advert_settings import AdvertSettings
from .timestamps import Timestamps


class CampaignsInformationItem(BaseType):
    """Campaigns Information"""

    bid_type: str = Field(alias="bid_type")
    id_: int = Field(alias="id")
    nm_settings: list[AdvertNmsSettings] = Field(alias="nm_settings")
    settings: AdvertSettings = Field(alias="settings")
    status: int = Field(alias="status")
    timestamps: Timestamps = Field(alias="timestamps")
