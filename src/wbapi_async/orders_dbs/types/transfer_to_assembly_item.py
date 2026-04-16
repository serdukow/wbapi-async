from pydantic import Field

from ...types.base import BaseType
from .api_batch_error_response import ApiBatchErrorResponse


class TransferToAssemblyItem(BaseType):
    """Transfer to Assembly"""

    errors: list[ApiBatchErrorResponse] | None = Field(None, alias="errors")
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
