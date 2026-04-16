from pydantic import Field

from ...types.base import BaseType


class NmBidsItem(BaseType):
    nm_id: int = Field()
    bid_kopecks: int = Field()
    placement: str = Field()
