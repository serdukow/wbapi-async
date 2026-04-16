from pydantic import Field

from ...types.base import BaseType


class DetailsForTheAcquiringExpensesReportsByReportIdResponse(BaseType):
    """Details for the Acquiring Expenses Reports by Report ID"""

    rrd_id: int = Field(alias="rrdId")
    report_id: int = Field(alias="reportId")
    acq_date: str = Field(alias="acqDate")
    acquiring_bank: str = Field(alias="acquiringBank")
    tin: str = Field()
    tax_registration_reason_code: str = Field(alias="taxRegistrationReasonCode")
    sale_date: str = Field(alias="saleDate")
    srid: str = Field()
    doc_type_name: str = Field(alias="docTypeName")
    nm_id: int = Field(alias="nmId")
    retail_amount: str = Field(alias="retailAmount")
    acquiring_fee: str = Field(alias="acquiringFee")
    acquiring_fee_vat: str = Field(alias="acquiringFeeVat")
    invoice_number: str = Field(alias="invoiceNumber")
    invoice_date: str = Field(alias="invoiceDate")
    shk_id: int = Field(alias="shkId")
    currency: str = Field()
