from pydantic import Field

from ...types.base import BaseType
from ..enums.supplier_status import SupplierStatus
from ..enums.wb_status import WbStatus


class AssemblyOrdersStatusesItem(BaseType):
    """Get Assembly Orders Statuses"""

    id_: int | None = Field(None, alias="id")
    supplier_status: SupplierStatus | None = Field(None, alias="supplierStatus")
    wb_status: WbStatus | None = Field(None, alias="wbStatus")
