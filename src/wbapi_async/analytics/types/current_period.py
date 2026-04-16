from pydantic import Field

from ...types.base import BaseType


class CurrentPeriod(BaseType):
    """Current period"""

    start: str = Field()
    end: str = Field()
