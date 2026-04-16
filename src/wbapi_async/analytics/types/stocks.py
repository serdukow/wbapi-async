from pydantic import Field

from ...types.base import BaseType


class Stocks(BaseType):
    """Inventory"""

    wb: int = Field()
    mp: int = Field()
    balance_sum: int = Field(alias="balanceSum")
