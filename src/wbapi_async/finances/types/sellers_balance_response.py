from pydantic import Field

from ...types.base import BaseType


class SellersBalanceResponse(BaseType):
    """Get Seller's Balance"""

    currency: str | None = Field(None)
    current: float | None = Field(None)
    for_withdraw: float | None = Field(None)
