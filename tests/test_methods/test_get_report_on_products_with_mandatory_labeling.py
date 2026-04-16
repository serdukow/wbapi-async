import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ReportOnProductsWithMandatoryLabelingItem


@pytest.mark.unit
class TestGetReportOnProductsWithMandatoryLabeling:
    async def test_get_report_on_products_with_mandatory_labeling(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "response": {
                    "data": [
                        {
                            "name": "Россия",
                            "price": 100,
                            "currency_name_short": "AMD",
                            "excise_short": "0102900254680370215_Re/=lSbNiGD",
                            "barcode": "2038893425820",
                            "nm_id": 169085355,
                            "operation_type_id": 1,
                            "fiscal_doc_number": 12345678,
                            "fiscal_dt": "2024-01-01",
                            "fiscal_drive_number": "fiscal_drive_number",
                            "rid": 606217433440,
                            "srid": "7513432034713632943.1.0",
                        }
                    ]
                }
            }
        )

        result = await api.get_report_on_products_with_mandatory_labeling(
            date_from="date_from", date_to="date_to"
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ReportOnProductsWithMandatoryLabelingItem)
        assert result[0].name == "Россия"
        assert result[0].price == 100
        assert result[0].currency_name_short == "AMD"
        assert result[0].excise_short == "0102900254680370215_Re/=lSbNiGD"
        assert result[0].barcode == "2038893425820"
