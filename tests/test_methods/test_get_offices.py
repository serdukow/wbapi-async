import pytest

from wbapi_async.types.offices_response import OfficesResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetOffices:

    async def test_get_offices(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "address": "address",
                "name": "name",
                "city": "city",
                "id": 1,
                "longitude": 1.0,
                "latitude": 1.0,
                "cargoType": 1,
                "deliveryType": 1,
                "federalDistrict": "federalDistrict",
                "selected": True,
            }]
        )

        result = await api.get_offices()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OfficesResponse)
        assert result[0].address == "address"
        assert result[0].name == "name"
        assert result[0].city == "city"
