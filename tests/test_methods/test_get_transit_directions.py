import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import TransitDirectionsResponse


@pytest.mark.unit
class TestGetTransitDirections:
    async def test_get_transit_directions(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "transitWarehouseName": "transitWarehouseName",
                    "destinationWarehouseName": "destinationWarehouseName",
                    "activeFrom": "activeFrom",
                    "boxTariff": [{"from": 1, "to": 1, "value": 1.0}],
                    "palletTariff": 1,
                }
            ]
        )

        result = await api.get_transit_directions()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], TransitDirectionsResponse)
        assert result[0].transit_warehouse_name == "transitWarehouseName"
        assert result[0].destination_warehouse_name == "destinationWarehouseName"
        assert result[0].active_from == "activeFrom"
        assert result[0].pallet_tariff == 1
