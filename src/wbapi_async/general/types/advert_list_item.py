from pydantic import Field

from ...types.base import BaseType


class AdvertListItem(BaseType):
    advert_id: int | None = Field(None, alias="advertId")
    change_time: str | None = Field(None, alias="changeTime")
