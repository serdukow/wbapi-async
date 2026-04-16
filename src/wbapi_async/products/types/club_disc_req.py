from pydantic import Field

from ...types.base import BaseType


class ClubDiscReq(BaseType):
    nm_id: int = Field(alias="nmID")
    club_discount: int = Field(alias="clubDiscount")
