from pydantic import Field

from ...types.base import BaseType


class BalanceItem(BaseType):
    """Balance"""

    sum_: int | None = Field(None, alias="sum")
    percent: int | None = Field(None, alias="percent")
    expiration_date: str | None = Field(None, alias="expiration_date")
