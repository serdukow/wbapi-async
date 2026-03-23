import pytest

from wbapi_async.types import ASuppliesListItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetASuppliesList:

    async def test_get_a_supplies_list(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "supplies": [{
                "id": "id",
                "isB2b": True,
                "done": True,
                "createdAt": "createdAt",
                "closedAt": "closedAt",
                "scanDt": "scanDt",
                "name": "name",
                "cargoType": 1,
                "crossBorderType": 1,
                "destinationOfficeId": 1,
            }]
        }
        )

        result = await api.get_a_supplies_list(limit=1, next_=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ASuppliesListItem)
        assert result[0].id_ == "id"
        assert result[0].is_b2b == True
        assert result[0].done == True
