from typing import Any

from pydantic import Field

from .base import BaseType


class GettingSellerPortalNewsItem(BaseType):
    """Getting Seller Portal News"""

    content: str | None = Field(None)
    date: str | None = Field(None)
    header: str | None = Field(None)
    id: int | None = Field(None)
    types: list[dict[str, Any]] | None = Field(None)
