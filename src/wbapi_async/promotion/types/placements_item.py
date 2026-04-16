from pydantic import Field

from ...types.base import BaseType
from .placements import Placements


class PlacementsItem(BaseType):
    advert_id: int = Field(alias="advert_id")
    placements: Placements = Field(alias="placements")
