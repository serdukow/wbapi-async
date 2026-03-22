from typing import Any

from pydantic import Field

from ...types.base import BaseType


class DocumentResponse(BaseType):
    """Get Document"""

    data: dict[str, Any] | None = Field(None)
