import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SalesReportListResponse


@pytest.mark.unit
class TestSalesReportList:
    async def test_sales_report_list(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "reportId": 1,
                    "sellerFinanceName": "sellerFinanceName",
                    "dateFrom": "dateFrom",
                    "dateTo": "dateTo",
                    "createDate": "createDate",
                    "currency": "currency",
                    "reportType": 1,
                    "retailAmountSum": "retailAmountSum",
                    "forPaySum": "forPaySum",
                    "avgSalePercent": 1.0,
                    "deliveryServiceSum": "deliveryServiceSum",
                    "paidStorageSum": "paidStorageSum",
                    "paidAcceptanceSum": "paidAcceptanceSum",
                    "deductionSum": "deductionSum",
                    "penaltySum": "penaltySum",
                    "additionalPaymentSum": "additionalPaymentSum",
                    "cashbackAmountSum": "cashbackAmountSum",
                    "cashbackDiscountSum": "cashbackDiscountSum",
                    "cashbackCommissionChangeSum": "cashbackCommissionChangeSum",
                    "paymentSchedule": "paymentSchedule",
                    "bankPaymentSum": "bankPaymentSum",
                }
            ]
        )

        result = await api.sales_report_list(date_from="date_from", date_to="date_to")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SalesReportListResponse)
        assert result[0].report_id == 1
        assert result[0].seller_finance_name == "sellerFinanceName"
        assert result[0].date_from == "dateFrom"
