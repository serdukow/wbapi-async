from pydantic import Field

from .base import BaseType


class AssemblyOrderStatusesItem(BaseType):
    """Get Assembly Order Statuses"""

    id: int | None = Field(None)
    supplier_status: str | None = Field(None, alias="supplierStatus")
    wb_status: str | None = Field(None, alias="wbStatus")
