from pydantic import Field

from ...types.base import BaseType


class TimeToReady(BaseType):
    days: int = Field()
    hours: int = Field()
    mins: int = Field()
