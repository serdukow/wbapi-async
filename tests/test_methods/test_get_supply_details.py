import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SupplyDetailsResponse


@pytest.mark.unit
class TestGetSupplyDetails:
    async def test_get_supply_details(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "id": "WB-GI-1234567",
                    "isB2b": True,
                    "done": True,
                    "createdAt": "2022-05-04T07:56:29Z",
                    "closedAt": "2022-05-04T07:56:29Z",
                    "scanDt": "2022-05-04T07:56:29Z",
                    "name": "My test supply",
                    "cargoType": 0,
                    "crossBorderType": 0,
                    "destinationOfficeId": 123,
                }
            ]
        )

        result = await api.get_supply_details(supply_id="supply_id")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SupplyDetailsResponse)
        assert result[0].id_ == "WB-GI-1234567"
        assert result[0].is_b2b
        assert result[0].done
        assert result[0].created_at == "2022-05-04T07:56:29Z"
        assert result[0].closed_at == "2022-05-04T07:56:29Z"
