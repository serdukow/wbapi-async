import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestAddAssemblyOrdersToTheSupply:

    async def test_add_assembly_orders_to_the_supply(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.add_assembly_orders_to_the_supply(supply_id="supply_id")

        assert result is None
