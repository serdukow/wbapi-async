from pydantic import Field

from ...types.base import BaseType


class OrdersStatusesItem(BaseType):
    """Get Orders Statuses"""

    id: int | None = Field(None)
    supplier_status: str | None = Field(None, alias="supplierStatus")
    wb_status: str | None = Field(None, alias="wbStatus")
