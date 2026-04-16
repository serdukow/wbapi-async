from pydantic import Field

from ...types.base import BaseType


class StocksItem(BaseType):
    chrt_id: int | None = Field(None, alias="chrtId")
    amount: int | None = Field(None)
