from pydantic import Field

from ...types.base import BaseType


class AssemblyOrdersStatusesItem(BaseType):
    """Get Assembly Orders Statuses"""

    id_: int | None = Field(None, alias="id")
    supplier_status: str | None = Field(None, alias="supplierStatus")
    wb_status: str | None = Field(None, alias="wbStatus")
