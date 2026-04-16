from pydantic import Field

from ...types.base import BaseType


class AnalyticsBrandShareItem(BaseType):
    """Get Report"""

    apply_date: str | None = Field(None, alias="applyDate")
    brand_rating: int | None = Field(None, alias="brandRating")
    price_percent: float | None = Field(None, alias="pricePercent")
    qty_percent: float | None = Field(None, alias="qtyPercent")
