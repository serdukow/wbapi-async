from pydantic import Field

from ...types.base import BaseType
from .api_batch_error_response import ApiBatchErrorResponse


class AddDataMatrixCodesToAssemblyOrdersChestnyZnakItem(BaseType):
    """Add Data Matrix Codes to Assembly Orders (Chestny ZNAK)"""

    errors: list[ApiBatchErrorResponse] | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
