import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDeleteTheSupply:
    async def test_delete_the_supply(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.delete_the_supply(supply_id="supply_id")

        assert result is None
