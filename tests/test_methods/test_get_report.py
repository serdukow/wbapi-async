import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ReportItem


@pytest.mark.unit
class TestGetReport:
    async def test_get_report(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "report": [
                    {
                        "cityName": "деревня Суханово",
                        "countryName": "Россия",
                        "foName": "Центральный федеральный округ",
                        "nmID": 177974431,
                        "regionName": "Московская область",
                        "sa": "112233445566778899",
                        "saleInvoiceCostPrice": 592.11,
                        "saleInvoiceCostPricePerc": 43.0547333297454,
                        "saleItemInvoiceQty": 4,
                    }
                ]
            }
        )

        result = await api.get_report(date_from="date_from", date_to="date_to")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ReportItem)
        assert result[0].city_name == "деревня Суханово"
        assert result[0].country_name == "Россия"
        assert result[0].fo_name == "Центральный федеральный округ"
        assert result[0].nm_id == 177974431
        assert result[0].region_name == "Московская область"
