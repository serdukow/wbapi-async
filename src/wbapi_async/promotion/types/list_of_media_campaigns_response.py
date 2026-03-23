from pydantic import Field

from ...types.base import BaseType


class ListOfMediaCampaignsResponse(BaseType):
    """List of Media Campaigns"""

    advert_id: int | None = Field(None, alias="advertId")
    name: str | None = Field(None)
    brand: str | None = Field(None)
    type_: int | None = Field(None, alias="type")
    status: int | None = Field(None)
    create_time: str | None = Field(None, alias="createTime")
    end_time: str | None = Field(None, alias="endTime")
