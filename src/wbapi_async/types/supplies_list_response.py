from typing import Any

from pydantic import Field

from .base import BaseType


class SuppliesListResponse(BaseType):
    """Supplies List"""

    phone: str | None = Field(None)
    supply_id: int | None = Field(None, alias="supplyID")
    preorder_id: int | None = Field(None, alias="preorderID")
    create_date: str | None = Field(None, alias="createDate")
    supply_date: str | None = Field(None, alias="supplyDate")
    fact_date: str | None = Field(None, alias="factDate")
    updated_date: str | None = Field(None, alias="updatedDate")
    status_id: int | None = Field(None, alias="statusID")
    box_type_id: Any | None = Field(None, alias="boxTypeID")
    is_box_on_pallet: bool | None = Field(None, alias="isBoxOnPallet")
