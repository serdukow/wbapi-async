import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SupplyBoxesListItem


@pytest.mark.unit
class TestGetSupplyBoxesList:
    async def test_get_supply_boxes_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "trbxes": [
                    {
                        "id": "WB-TRBX-1234567",
                    }
                ]
            }
        )

        result = await api.get_supply_boxes_list(supply_id="supply_id")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SupplyBoxesListItem)
        assert result[0].id_ == "WB-TRBX-1234567"
