from typing import Any

from pydantic import Field

from .base import BaseType


class B2BBuyerInformationItem(BaseType):
    """B2B Buyer Information"""

    data: dict[str, Any] | None = Field(None)
    errors: list[dict[str, Any]] | None = Field(None)
    is_error: bool = Field(None, alias="isError")
    order_id: int = Field(None, alias="orderId")
