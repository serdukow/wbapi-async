from pydantic import Field

from ...types.base import BaseType
from ..enums.payment_type import PaymentType
from .placements import Placements


class AdvertSettings(BaseType):
    """Campaign settings"""

    payment_type: PaymentType = Field()
    name: str = Field()
    placements: Placements = Field()
