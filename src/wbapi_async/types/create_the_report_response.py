from typing import Any

from pydantic import Field

from .base import BaseType


class CreateTheReportResponse(BaseType):
    """Create the Report"""

    data: dict[str, Any] | None = Field(None)
