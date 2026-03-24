import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestMoveTheSupplyToTheDelivery:
    async def test_move_the_supply_to_the_delivery(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.move_the_supply_to_the_delivery(supply_id="supply_id")

        assert result is None
