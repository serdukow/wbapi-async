from pydantic import Field

from ...types.base import BaseType


class V0SetNormQueryBidsRequestItem(BaseType):
    advert_id: int = Field()
    nm_id: int = Field()
    norm_query: str = Field()
    bid: int = Field()
