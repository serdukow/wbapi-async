from pydantic import Field

from ...types.base import BaseType
from .placements import Placements


class AdvertSettings(BaseType):
    """Campaign settings"""

    payment_type: str = Field(alias="payment_type")
    name: str = Field(alias="name")
    placements: Placements = Field(alias="placements")
