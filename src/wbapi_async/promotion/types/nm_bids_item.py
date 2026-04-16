from pydantic import Field

from ...types.base import BaseType


class NmBidsItem(BaseType):
    nm_id: int = Field(alias="nm_id")
    bid_kopecks: int = Field(alias="bid_kopecks")
    placement: str = Field(alias="placement")
