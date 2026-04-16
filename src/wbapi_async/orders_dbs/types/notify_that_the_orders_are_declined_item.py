from pydantic import Field

from ...types.base import BaseType
from .api_batch_error_response import ApiBatchErrorResponse


class NotifyThatTheOrdersAreDeclinedItem(BaseType):
    """Notify that the Orders Are Declined"""

    errors: list[ApiBatchErrorResponse] | None = Field(None, alias="errors")
    is_error: bool | None = Field(None, alias="isError")
    order_id: int | None = Field(None, alias="orderId")
