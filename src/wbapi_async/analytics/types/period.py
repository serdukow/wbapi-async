from pydantic import Field

from ...types.base import BaseType


class Period(BaseType):
    start: str = Field()
    end: str = Field()
