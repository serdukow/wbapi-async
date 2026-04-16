from pydantic import Field

from ...types.base import BaseType


class SaleRate(BaseType):
    """Current DSI. Special cases: 1) `"hours":-1` — infinite duration 2) `"hours":-2` — zero duration 3..."""

    days: int = Field()
    hours: int = Field()
