from pydantic import Field

from ...orders_dbs.types.api_batch_error_response import ApiBatchErrorResponse
from ...types.base import BaseType


class NotifyThatTheOrdersWereReceivedByTheBuyersItem(BaseType):
    """Notify That the Orders Were Received by the Buyers"""

    order_id: int = Field(alias="orderId")
    is_error: bool = Field(alias="isError")
    errors: list[ApiBatchErrorResponse] | None = Field(None)
