from typing import Any

from pydantic import Field

from ...types.base import BaseType


class DocumentsResponse(BaseType):
    """Get Documents"""

    data: dict[str, Any] | None = Field(None)
