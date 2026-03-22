from pydantic import Field

from .base import BaseType


class ReturnTariffsItem(BaseType):
    """Return Tariffs"""

    delivery_dump_kgt_office_base: str | None = Field(None, alias="deliveryDumpKgtOfficeBase")
    delivery_dump_kgt_office_liter: str | None = Field(None, alias="deliveryDumpKgtOfficeLiter")
    delivery_dump_kgt_return_expr: str | None = Field(None, alias="deliveryDumpKgtReturnExpr")
    delivery_dump_srg_office_expr: str | None = Field(None, alias="deliveryDumpSrgOfficeExpr")
    delivery_dump_srg_return_expr: str | None = Field(None, alias="deliveryDumpSrgReturnExpr")
    delivery_dump_sup_courier_base: str | None = Field(None, alias="deliveryDumpSupCourierBase")
    delivery_dump_sup_courier_liter: str | None = Field(None, alias="deliveryDumpSupCourierLiter")
    delivery_dump_sup_office_base: str | None = Field(None, alias="deliveryDumpSupOfficeBase")
    delivery_dump_sup_office_liter: str | None = Field(None, alias="deliveryDumpSupOfficeLiter")
    delivery_dump_sup_return_expr: str | None = Field(None, alias="deliveryDumpSupReturnExpr")
    warehouse_name: str | None = Field(None, alias="warehouseName")
