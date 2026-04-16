import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestUpdateInventory:
    async def test_update_inventory(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.update_inventory(warehouse_id=1, stocks=[{"chrtId": 12345678, "amount": 10}])

        assert result is None
