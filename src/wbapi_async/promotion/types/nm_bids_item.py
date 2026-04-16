from pydantic import Field

from ...types.base import BaseType
from ..enums.placement import Placement


class NmBidsItem(BaseType):
    nm_id: int = Field()
    bid_kopecks: int = Field()
    placement: Placement = Field()
