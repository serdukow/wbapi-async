from typing import Any

from pydantic import Field

from ...types.base import BaseType


class PaginationByGroupsResponse(BaseType):
    """Pagination by Groups"""

    data: dict[str, Any] = Field(alias="data")
