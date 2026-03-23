import pytest

from wbapi_async.types import AddBoxesToTheSupplyItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestAddBoxesToTheSupply:

    async def test_add_boxes_to_the_supply(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "trbxIds": [{

            }]
        }
        )

        result = await api.add_boxes_to_the_supply(supply_id="supply_id", amount=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AddBoxesToTheSupplyItem)
