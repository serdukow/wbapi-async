from pydantic import Field

from ...types.base import BaseType


class GoodCard(BaseType):
    """Order information"""

    date: str | None = Field(None, alias="date")
    nm_id: int | None = Field(None, alias="nmID")
    price: int | None = Field(None, alias="price")
    price_currency: str | None = Field(None, alias="priceCurrency")
    rid: str | None = Field(None, alias="rid")
    size: str | None = Field(None, alias="size")
