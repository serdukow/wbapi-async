from pydantic import Field

from ...types.base import BaseType
from .nms import Nms


class NmsItem(BaseType):
    advert_id: int = Field()
    nms: Nms = Field()
