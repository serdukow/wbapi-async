from pydantic import Field

from ...types.base import BaseType


class GoodCard(BaseType):
    """Order information"""

    date: str | None = Field(None)
    nm_id: int | None = Field(None, alias="nmID")
    price: int | None = Field(None)
    price_currency: str | None = Field(None, alias="priceCurrency")
    rid: str | None = Field(None)
    size: str | None = Field(None)
