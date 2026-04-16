from pydantic import Field

from ...types.base import BaseType
from .api_batch_error_response import ApiBatchErrorResponse


class TransferToDeliveryItem(BaseType):
    """Transfer to Delivery"""

    errors: list[ApiBatchErrorResponse] | None = Field(None)
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
