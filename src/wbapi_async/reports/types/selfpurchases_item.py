from pydantic import Field

from ...types.base import BaseType


class SelfpurchasesItem(BaseType):
    """Self-purchases"""

    nm_id: int | None = Field(None, alias="nmID")
    sum_: int | None = Field(None, alias="sum")
    currency: str | None = Field(None)
    date_from: str | None = Field(None, alias="dateFrom")
    date_to: str | None = Field(None, alias="dateTo")
