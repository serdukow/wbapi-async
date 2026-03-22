from pydantic import Field

from .base import BaseType


class RegenerateTheReportResponse(BaseType):
    """Regenerate the Report"""

    data: str = Field(None)
