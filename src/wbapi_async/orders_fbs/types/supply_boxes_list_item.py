from pydantic import Field

from ...types.base import BaseType


class SupplyBoxesListItem(BaseType):
    """Get Supply Boxes List"""

    id_: str | None = Field(None, alias="id")
