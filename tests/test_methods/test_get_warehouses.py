import pytest

from wbapi_async.types.get_warehouses_response import GetWarehousesResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetWarehouses:

    async def test_get_warehouses(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "name": "name",
                "officeId": 1,
                "id": 1,
                "cargoType": 1,
                "deliveryType": 1,
                "isDeleting": True,
                "isProcessing": True,
            }]
        )

        result = await api.get_warehouses()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GetWarehousesResponse)
        assert result[0].name == "name"
        assert result[0].office_id == 1
        assert result[0].id == 1
