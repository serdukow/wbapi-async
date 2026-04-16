from pydantic import Field

from ...types.base import BaseType
from ..enums.status_2 import Status2
from .advert_n_ms_settings import AdvertNMsSettings
from .advert_settings import AdvertSettings
from .timestamps import Timestamps


class CampaignsInformationItem(BaseType):
    """Campaigns Information"""

    bid_type: str = Field()
    id_: int = Field(alias="id")
    nm_settings: list[AdvertNMsSettings] = Field()
    settings: AdvertSettings = Field()
    status: Status2 = Field()
    timestamps: Timestamps = Field()
