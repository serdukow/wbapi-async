from pydantic import Field

from ...types.base import BaseType


class SupplyBoxesListItem(BaseType):
    """Get Supply Boxes List"""

    id: str | None = Field(None)
