from typing import Any

from pydantic import Field

from ...types.base import BaseType


class OrdersAndPositionsByProductSearchTextsResponse(BaseType):
    """Orders and Positions by Product Search Texts"""

    data: dict[str, Any] = Field()
