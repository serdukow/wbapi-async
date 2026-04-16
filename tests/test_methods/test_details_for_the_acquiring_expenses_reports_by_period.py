import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import DetailsForTheAcquiringExpensesReportsByPeriodResponse


@pytest.mark.unit
class TestDetailsForTheAcquiringExpensesReportsByPeriod:
    async def test_details_for_the_acquiring_expenses_reports_by_period(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "rrdId": 1,
                    "reportId": 1,
                    "acqDate": "acqDate",
                    "acquiringBank": "acquiringBank",
                    "tin": "tin",
                    "taxRegistrationReasonCode": "taxRegistrationReasonCode",
                    "saleDate": "saleDate",
                    "srid": "srid",
                    "docTypeName": "docTypeName",
                    "nmId": 1,
                    "retailAmount": "retailAmount",
                    "acquiringFee": "acquiringFee",
                    "acquiringFeeVat": "acquiringFeeVat",
                    "invoiceNumber": "invoiceNumber",
                    "invoiceDate": "invoiceDate",
                    "shkId": 1,
                    "currency": "currency",
                }
            ]
        )

        result = await api.details_for_the_acquiring_expenses_reports_by_period(
            date_from="date_from", date_to="date_to"
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DetailsForTheAcquiringExpensesReportsByPeriodResponse)
        assert result[0].rrd_id == 1
        assert result[0].report_id == 1
        assert result[0].acq_date == "acqDate"
