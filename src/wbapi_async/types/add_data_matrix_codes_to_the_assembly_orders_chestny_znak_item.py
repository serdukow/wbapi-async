from typing import Any

from pydantic import Field

from .base import BaseType


class AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem(BaseType):
    """Add Data Matrix Codes to the Assembly Orders (Chestny ZNAK)"""

    order_id: int = Field(None, alias="orderId")
    is_error: bool = Field(None, alias="isError")
    errors: list[Any] | None = Field(None)
