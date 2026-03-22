from pydantic import Field

from .base import BaseType


class ReportOnProductsWithMandatoryLabelingItem(BaseType):
    """Report on Products with Mandatory Labeling"""

    name: str | None = Field(None)
    price: float | None = Field(None)
    currency_name_short: str | None = Field(None)
    excise_short: str | None = Field(None)
    barcode: str | None = Field(None)
    nm_id: int | None = Field(None)
    operation_type_id: int | None = Field(None)
    fiscal_doc_number: int | None = Field(None)
    fiscal_dt: str | None = Field(None)
    fiscal_drive_number: str | None = Field(None)
    rid: int | None = Field(None)
    srid: str | None = Field(None)
