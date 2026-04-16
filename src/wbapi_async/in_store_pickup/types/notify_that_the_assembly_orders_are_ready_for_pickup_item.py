from pydantic import Field

from ...orders_dbs.types.api_batch_error_response import ApiBatchErrorResponse
from ...types.base import BaseType


class NotifyThatTheAssemblyOrdersAreReadyForPickupItem(BaseType):
    """Notify That the Assembly Orders Are Ready for Pickup"""

    order_id: int = Field(alias="orderId")
    is_error: bool = Field(alias="isError")
    errors: list[ApiBatchErrorResponse] | None = Field(None)
