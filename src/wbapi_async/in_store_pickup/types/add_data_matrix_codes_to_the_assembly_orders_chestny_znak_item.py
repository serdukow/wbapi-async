from typing import Any

from pydantic import Field

from ...types.base import BaseType


class AddDataMatrixCodesToTheAssemblyOrdersChestnyZnakItem(BaseType):
    """Add Data Matrix Codes to the Assembly Orders (Chestny ZNAK)"""

    order_id: int = Field(alias="orderId")
    is_error: bool = Field(alias="isError")
    errors: list[Any] | None = Field(None)
