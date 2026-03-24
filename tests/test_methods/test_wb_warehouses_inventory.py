import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import WbWarehousesInventoryItem


@pytest.mark.unit
class TestWbWarehousesInventory:
    async def test_wb_warehouses_inventory(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "items": [
                        {
                            "nmId": 1,
                            "chrtId": 1,
                            "warehouseId": 1,
                            "warehouseName": "warehouseName",
                            "regionName": "regionName",
                            "quantity": 1,
                            "inWayToClient": 1,
                            "inWayFromClient": 1,
                        }
                    ]
                }
            }
        )

        result = await api.wb_warehouses_inventory()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], WbWarehousesInventoryItem)
        assert result[0].nm_id == 1
        assert result[0].chrt_id == 1
        assert result[0].warehouse_id == 1
