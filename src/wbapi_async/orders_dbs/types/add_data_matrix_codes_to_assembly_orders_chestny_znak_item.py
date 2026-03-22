from typing import Any

from pydantic import Field

from ...types.base import BaseType


class AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem(BaseType):
    """Add Data Matrix Codes to Assembly Orders (Chestny ZNAK)"""

    errors: list[Any] | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
