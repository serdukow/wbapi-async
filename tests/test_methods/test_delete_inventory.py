import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDeleteInventory:
    async def test_delete_inventory(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.delete_inventory(warehouse_id=1, chrt_ids=[])

        assert result is None
