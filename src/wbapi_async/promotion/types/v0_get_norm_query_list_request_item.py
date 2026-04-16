from pydantic import Field

from ...types.base import BaseType


class V0GetNormQueryListRequestItem(BaseType):
    advert_id: int = Field(alias="advertId")
    nm_id: int = Field(alias="nmId")
