from pydantic import Field

from ...types.base import BaseType


class ReportOnProductsWithMandatoryLabelingItem(BaseType):
    """Report on Products with Mandatory Labeling"""

    name: str | None = Field(None, alias="name")
    price: float | None = Field(None, alias="price")
    currency_name_short: str | None = Field(None, alias="currency_name_short")
    excise_short: str | None = Field(None, alias="excise_short")
    barcode: str | None = Field(None, alias="barcode")
    nm_id: int | None = Field(None, alias="nm_id")
    operation_type_id: int | None = Field(None, alias="operation_type_id")
    fiscal_doc_number: int | None = Field(None, alias="fiscal_doc_number")
    fiscal_dt: str | None = Field(None, alias="fiscal_dt")
    fiscal_drive_number: str | None = Field(None, alias="fiscal_drive_number")
    rid: int | None = Field(None, alias="rid")
    srid: str | None = Field(None, alias="srid")
