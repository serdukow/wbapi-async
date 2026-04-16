from pydantic import Field

from ...types.base import BaseType


class V0GetNormQueryBidsRequestItem(BaseType):
    advert_id: int = Field(alias="advert_id")
    nm_id: int = Field(alias="nm_id")
