import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDeleteWarehouse:

    async def test_delete_warehouse(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.delete_warehouse(warehouse_id=1)

        assert result is None
