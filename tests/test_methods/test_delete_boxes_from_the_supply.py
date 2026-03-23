import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDeleteBoxesFromTheSupply:
    async def test_delete_boxes_from_the_supply(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.delete_boxes_from_the_supply(supply_id="supply_id", trbx_ids=[])

        assert result is None
