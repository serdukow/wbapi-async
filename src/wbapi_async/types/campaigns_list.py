from pydantic import Field

from .base import BaseType


class CampaignItem(BaseType):
    advert_id: int | None = Field(None, alias="advertId")
    change_time: str | None = Field(None, alias="changeTime")


class CampaignGroup(BaseType):
    type: int | None = Field(None, alias="type")
    status: int | None = Field(None, alias="status")
    count: int | None = Field(None, alias="count")
    advert_list: list[CampaignItem] | None = Field(None, alias="advert_list")


class CampaignsList(BaseType):
    adverts: list[CampaignGroup] | None = Field(None, alias="adverts")
    all: int | None = Field(None, alias="all")
