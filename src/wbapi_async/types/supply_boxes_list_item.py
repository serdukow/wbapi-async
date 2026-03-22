from pydantic import Field

from .base import BaseType


class SupplyBoxesListItem(BaseType):
    """Get Supply Boxes List"""

    id: str | None = Field(None)
