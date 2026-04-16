from pydantic import Field

from ...types.base import BaseType


class AcquiringExpensesReportListResponse(BaseType):
    """Acquiring Expenses Report List"""

    report_id: int = Field(alias="reportId")
    seller_finance_name: str = Field(alias="sellerFinanceName")
    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    create_date: str = Field(alias="createDate")
    currency: str = Field()
    acquiring_fee_sum: str = Field(alias="acquiringFeeSum")
    acquiring_fee_vat_sum: str = Field(alias="acquiringFeeVatSum")
