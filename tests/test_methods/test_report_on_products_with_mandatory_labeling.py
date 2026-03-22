import pytest

from wbapi_async.types.report_on_products_with_mandatory_labeling_item import ReportOnProductsWithMandatoryLabelingItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestReportOnProductsWithMandatoryLabeling:

    async def test_report_on_products_with_mandatory_labeling(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "response": {
            "data": [{
                "name": "name",
                "price": 1.0,
                "currency_name_short": "currency_name_short",
                "excise_short": "excise_short",
                "barcode": "barcode",
                "nm_id": 1,
                "operation_type_id": 1,
                "fiscal_doc_number": 1,
                "fiscal_dt": "fiscal_dt",
                "fiscal_drive_number": "fiscal_drive_number",
                "rid": 1,
                "srid": "srid",
            }]
        }
        }
        )

        result = await api.report_on_products_with_mandatory_labeling(date_from="date_from", date_to="date_to")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ReportOnProductsWithMandatoryLabelingItem)
        assert result[0].name == "name"
        assert result[0].price == 1.0
        assert result[0].currency_name_short == "currency_name_short"
