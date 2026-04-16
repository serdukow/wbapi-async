from pydantic import Field

from ...types.base import BaseType


class SellersBalanceResponse(BaseType):
    """Get Seller's Balance"""

    currency: str | None = Field(None, alias="currency")
    current: float | None = Field(None, alias="current")
    for_withdraw: float | None = Field(None, alias="for_withdraw")
