from pydantic import Field

from ...types.base import BaseType


class SizeGoodReq(BaseType):
    nm_id: int = Field(alias="nmID")
    size_id: int = Field(alias="sizeID")
    price: int = Field()
