import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import DetailsForTheAcquiringExpensesReportsByReportIdResponse


@pytest.mark.unit
class TestDetailsForTheAcquiringExpensesReportsByReportId:
    async def test_details_for_the_acquiring_expenses_reports_by_report_id(self, api: MockedAPI) -> None:
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

        result = await api.details_for_the_acquiring_expenses_reports_by_report_id(report_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DetailsForTheAcquiringExpensesReportsByReportIdResponse)
        assert result[0].rrd_id == 1
        assert result[0].report_id == 1
        assert result[0].acq_date == "acqDate"
