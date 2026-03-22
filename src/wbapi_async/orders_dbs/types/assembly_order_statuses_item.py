from typing import Any

from pydantic import Field

from ...types.base import BaseType


class AssemblyOrderStatusesItem(BaseType):
    """Get Assembly Order Statuses"""

    errors: list[Any] | None = Field(None)
    order_id: int | None = Field(None, alias="orderId")
    supplier_status: str | None = Field(None, alias="supplierStatus")
    wb_status: str | None = Field(None, alias="wbStatus")
