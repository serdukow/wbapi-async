from typing import Any

from pydantic import Field

from ...types.base import BaseType


class PaginationByProductsWithinAGroupResponse(BaseType):
    """Pagination by Products Within a Group"""

    data: dict[str, Any] = Field()
