from pydantic import Field

from ...types.base import BaseType
from .api_orders_error_response import ApiOrdersErrorResponse


class DeleteAssemblyOrderMetadataItem(BaseType):
    """Delete Assembly Order Metadata"""

    order_id: int = Field(alias="orderId")
    is_error: bool = Field(alias="isError")
    errors: list[ApiOrdersErrorResponse] | None = Field(None)
