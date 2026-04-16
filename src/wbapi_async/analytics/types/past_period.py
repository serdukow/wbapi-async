from pydantic import Field

from ...types.base import BaseType


class PastPeriod(BaseType):
    start: str = Field()
    end: str = Field()
