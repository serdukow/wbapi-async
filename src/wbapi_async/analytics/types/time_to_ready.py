from pydantic import Field

from ...types.base import BaseType


class TimeToReady(BaseType):
    days: int = Field(alias="days")
    hours: int = Field(alias="hours")
    mins: int = Field(alias="mins")
