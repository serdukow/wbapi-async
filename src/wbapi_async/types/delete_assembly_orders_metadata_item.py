from typing import Any

from pydantic import Field

from .base import BaseType


class DeleteAssemblyOrdersMetadataItem(BaseType):
    """Delete Assembly Orders Metadata"""

    errors: list[Any] | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
