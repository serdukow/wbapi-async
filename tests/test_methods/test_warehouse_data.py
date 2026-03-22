import pytest

from wbapi_async.types.warehouse_data_item import WarehouseDataItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestWarehouseData:

    async def test_warehouse_data(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": {
            "regions": [{
                "regionName": "regionName",
                "metrics": None,
                "offices": [],
            }]
        }
        }
        )

        result = await api.warehouse_data()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], WarehouseDataItem)
        assert result[0].region_name == "regionName"
        assert result[0].offices == []
