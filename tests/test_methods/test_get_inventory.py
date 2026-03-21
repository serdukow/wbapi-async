import pytest

from wbapi_async.types.get_inventory_item import GetInventoryItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetInventory:

    async def test_get_inventory(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "stocks": [{
                "chrtId": 1,
                "amount": 1,
            }]
        }
        )

        result = await api.get_inventory(warehouse_id=1, chrt_ids=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GetInventoryItem)
        assert result[0].chrt_id == 1
        assert result[0].amount == 1
