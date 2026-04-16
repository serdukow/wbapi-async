import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import WarehousesResponse


@pytest.mark.unit
class TestGetWarehouses:
    async def test_get_warehouses(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "name": "Kosmonavtov 14",
                    "officeId": 15,
                    "id": 1,
                    "cargoType": "1",
                    "deliveryType": "1",
                    "isDeleting": False,
                    "isProcessing": True,
                }
            ]
        )

        result = await api.get_warehouses()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], WarehousesResponse)
        assert result[0].name == "Kosmonavtov 14"
        assert result[0].office_id == 15
        assert result[0].id_ == 1
        assert result[0].cargo_type == "1"
        assert result[0].delivery_type == "1"
