from pydantic import Field

from ...types.base import BaseType


class ProductLabelingItem(BaseType):
    """Product Labeling"""

    amount: float | None = Field(None, alias="amount")
    date: str | None = Field(None, alias="date")
    income_id: int | None = Field(None, alias="incomeId")
    nm_id: int | None = Field(None, alias="nmID")
    photo_urls: list[str] | None = Field(None, alias="photoUrls")
    shk_id: int | None = Field(None, alias="shkID")
    sku: str | None = Field(None, alias="sku")
