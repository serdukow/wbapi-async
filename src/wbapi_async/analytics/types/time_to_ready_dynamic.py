from pydantic import Field

from ...types.base import BaseType


class TimeToReadyDynamic(BaseType):
    days: int = Field()
    hours: int = Field()
    mins: int = Field()
