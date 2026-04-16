from pydantic import Field

from ...types.base import BaseType


class CreateTheReportResponse(BaseType):
    """Create the Report"""

    data: str = Field(alias="data")
