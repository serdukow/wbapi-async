import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AcquiringExpensesReportListResponse


@pytest.mark.unit
class TestAcquiringExpensesReportList:
    async def test_acquiring_expenses_report_list(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "reportId": 1,
                    "sellerFinanceName": "sellerFinanceName",
                    "dateFrom": "dateFrom",
                    "dateTo": "dateTo",
                    "createDate": "createDate",
                    "currency": "currency",
                    "acquiringFeeSum": "acquiringFeeSum",
                    "acquiringFeeVatSum": "acquiringFeeVatSum",
                }
            ]
        )

        result = await api.acquiring_expenses_report_list(date_from="date_from", date_to="date_to")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AcquiringExpensesReportListResponse)
        assert result[0].report_id == 1
        assert result[0].seller_finance_name == "sellerFinanceName"
        assert result[0].date_from == "dateFrom"
