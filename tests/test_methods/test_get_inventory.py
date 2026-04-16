import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import InventoryItem


@pytest.mark.unit
class TestGetInventory:
    async def test_get_inventory(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "stocks": [
                    {
                        "chrtId": 12345678,
                        "amount": 10,
                    }
                ]
            }
        )

        result = await api.get_inventory(warehouse_id=1, chrt_ids=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], InventoryItem)
        assert result[0].chrt_id == 12345678
        assert result[0].amount == 10
