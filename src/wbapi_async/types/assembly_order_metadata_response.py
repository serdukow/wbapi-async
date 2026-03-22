from typing import Any

from pydantic import Field

from .base import BaseType


class AssemblyOrderMetadataResponse(BaseType):
    """Get Assembly Order Metadata"""

    meta: dict[str, Any] | None = Field(None)
