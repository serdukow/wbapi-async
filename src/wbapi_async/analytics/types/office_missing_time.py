from pydantic import Field

from ...types.base import BaseType


class OfficeMissingTime(BaseType):
    """Out-of-stock time. Special cases: 1) `"hours":-1` — infinite duration 2) `"hours":-2` — zero dura..."""

    days: int = Field()
    hours: int = Field()
