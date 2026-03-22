from typing import Any

from pydantic import Field

from ...types.base import BaseType


class MinimumBidsForProductCardsItem(BaseType):
    """Minimum Bids for Product Cards"""

    bids: list[dict[str, Any]] = Field()
    nm_id: int = Field()
