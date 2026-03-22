from pydantic import Field

from ...types.base import BaseType


class HiddenFromTheCatalogItem(BaseType):
    """Hidden from the Catalog"""

    brand: str | None = Field(None)
    nm_id: int | None = Field(None, alias="nmId")
    title: str | None = Field(None)
    vendor_code: str | None = Field(None, alias="vendorCode")
    nm_rating: float | None = Field(None, alias="nmRating")
