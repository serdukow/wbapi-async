from pydantic import Field

from ...types.base import BaseType


class Placements(BaseType):
    """Placements"""

    search: bool = Field()
    recommendations: bool = Field()
