import pytest

from wbapi_async.types.report_item import ReportItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetReport:

    async def test_get_report(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "report": [{
                "cityName": "cityName",
                "countryName": "countryName",
                "foName": "foName",
                "nmID": 1,
                "regionName": "regionName",
                "sa": "sa",
                "saleInvoiceCostPrice": 1.0,
                "saleInvoiceCostPricePerc": 1.0,
                "saleItemInvoiceQty": 1,
            }]
        }
        )

        result = await api.get_report(date_from="date_from", date_to="date_to")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ReportItem)
        assert result[0].city_name == "cityName"
        assert result[0].country_name == "countryName"
        assert result[0].fo_name == "foName"
