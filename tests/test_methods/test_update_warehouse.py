import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestUpdateWarehouse:
    async def test_update_warehouse(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.update_warehouse(warehouse_id=1, name="name", office_id=1)

        assert result is None
