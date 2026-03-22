from typing import Any

from pydantic import Field

from .base import BaseType


class GenerateTheReportResponse(BaseType):
    """Generate the Report"""

    data: dict[str, Any] | None = Field(None)
