from pydantic import Field

from ...types.base import BaseType


class RegenerateTheReportResponse(BaseType):
    """Regenerate the Report"""

    data: str = Field(alias="data")
