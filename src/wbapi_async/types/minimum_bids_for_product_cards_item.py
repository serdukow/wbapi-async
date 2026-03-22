from typing import Any

from pydantic import Field

from .base import BaseType


class MinimumBidsForProductCardsItem(BaseType):
    """Minimum Bids for Product Cards"""

    bids: list[dict[str, Any]] = Field(None)
    nm_id: int = Field(None)
