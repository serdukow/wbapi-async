from typing import Any

from pydantic import Field

from ...types.base import BaseType


class AssemblyOrdersMetadataItem(BaseType):
    """Get Assembly Orders Metadata"""

    id: int | None = Field(None)
    meta: dict[str, Any] | None = Field(None)
