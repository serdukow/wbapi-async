from pydantic import Field

from ...types.base import BaseType


class Stocks(BaseType):
    """Inventory"""

    wb: int = Field(alias="wb")
    mp: int = Field(alias="mp")
    balance_sum: int = Field(alias="balanceSum")
