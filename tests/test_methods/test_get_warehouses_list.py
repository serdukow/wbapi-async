import pytest

from wbapi_async.types.warehouses_list_response import WarehousesListResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetWarehousesList:

    async def test_get_warehouses_list(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "ID": 1,
                "name": "name",
                "address": "address",
                "workTime": "workTime",
                "isActive": True,
                "isTransitActive": True,
            }]
        )

        result = await api.get_warehouses_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], WarehousesListResponse)
        assert result[0].id == 1
        assert result[0].name == "name"
        assert result[0].address == "address"
