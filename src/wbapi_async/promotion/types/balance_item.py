from pydantic import Field

from ...types.base import BaseType


class BalanceItem(BaseType):
    """Balance"""

    sum: int | None = Field(None)
    percent: int | None = Field(None)
    expiration_date: str | None = Field(None)
