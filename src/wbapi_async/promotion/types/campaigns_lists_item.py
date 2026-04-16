from pydantic import Field

from ...types.base import BaseType
from .advert_list_item import AdvertListItem


class CampaignsListsItem(BaseType):
    """Campaigns Lists"""

    type_: int | None = Field(None, alias="type")
    status: int | None = Field(None, alias="status")
    count: int | None = Field(None, alias="count")
    advert_list: list[AdvertListItem] | None = Field(None, alias="advert_list")
