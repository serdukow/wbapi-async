from typing import Any

from pydantic import Field

from ...types.base import BaseType


class TransferToAssemblyItem(BaseType):
    """Transfer to Assembly"""

    errors: list[Any] | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
