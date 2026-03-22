from typing import Any

from pydantic import Field

from ...types.base import BaseType


class CheckTheStatusResponse(BaseType):
    """Check the Status"""

    data: dict[str, Any] | None = Field(None)
