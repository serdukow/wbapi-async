from pydantic import Field

from .base import BaseType


class AssemblyOrdersStatusesItem(BaseType):
    """Get Assembly Orders Statuses"""

    id: int | None = Field(None)
    supplier_status: str | None = Field(None, alias="supplierStatus")
    wb_status: str | None = Field(None, alias="wbStatus")
