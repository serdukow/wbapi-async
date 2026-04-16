from pydantic import Field

from ...types.base import BaseType


class SalesReportListResponse(BaseType):
    """Sales Report List"""

    report_id: int = Field(alias="reportId")
    seller_finance_name: str = Field(alias="sellerFinanceName")
    date_from: str = Field(alias="dateFrom")
    date_to: str = Field(alias="dateTo")
    create_date: str = Field(alias="createDate")
    currency: str = Field()
    report_type: int = Field(alias="reportType")
    retail_amount_sum: str = Field(alias="retailAmountSum")
    for_pay_sum: str = Field(alias="forPaySum")
    avg_sale_percent: float = Field(alias="avgSalePercent")
    delivery_service_sum: str = Field(alias="deliveryServiceSum")
    paid_storage_sum: str = Field(alias="paidStorageSum")
    paid_acceptance_sum: str = Field(alias="paidAcceptanceSum")
    deduction_sum: str = Field(alias="deductionSum")
    penalty_sum: str = Field(alias="penaltySum")
    additional_payment_sum: str = Field(alias="additionalPaymentSum")
    cashback_amount_sum: str = Field(alias="cashbackAmountSum")
    cashback_discount_sum: str = Field(alias="cashbackDiscountSum")
    cashback_commission_change_sum: str = Field(alias="cashbackCommissionChangeSum")
    payment_schedule: str = Field(alias="paymentSchedule")
    bank_payment_sum: str = Field(alias="bankPaymentSum")
