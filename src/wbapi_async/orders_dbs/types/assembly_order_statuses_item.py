from pydantic import Field

from ...types.base import BaseType
from .api_batch_error_response import ApiBatchErrorResponse


class AssemblyOrderStatusesItem(BaseType):
    """Get Assembly Order Statuses"""

    errors: list[ApiBatchErrorResponse] | None = Field(None)
    order_id: int | None = Field(None, alias="orderId")
    supplier_status: str | None = Field(None, alias="supplierStatus")
    wb_status: str | None = Field(None, alias="wbStatus")
