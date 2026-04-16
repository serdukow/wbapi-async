from pydantic import Field

from ...types.base import BaseType


class SelectedPeriod(BaseType):
    start: str = Field(alias="start")
    end: str = Field(alias="end")
