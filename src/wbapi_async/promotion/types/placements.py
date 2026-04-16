from pydantic import Field

from ...types.base import BaseType


class Placements(BaseType):
    """Placements"""

    search: bool = Field(alias="search")
    recommendations: bool = Field(alias="recommendations")
