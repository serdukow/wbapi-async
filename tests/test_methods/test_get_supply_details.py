import pytest

from wbapi_async.types import SupplyDetailsResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetSupplyDetails:

    async def test_get_supply_details(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "id": "id",
                "isB2b": True,
                "done": True,
                "createdAt": "createdAt",
                "closedAt": "closedAt",
                "scanDt": "scanDt",
                "name": "name",
                "cargoType": 1,
                "crossBorderType": 1,
                "destinationOfficeId": 1,
            }]
        )

        result = await api.get_supply_details(supply_id="supply_id")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SupplyDetailsResponse)
        assert result[0].id == "id"
        assert result[0].is_b2b == True
        assert result[0].done == True
