import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SuppliesListResponse


@pytest.mark.unit
class TestGetSuppliesList:
    async def test_get_supplies_list(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "phone": "phone",
                    "supplyID": 1,
                    "preorderID": 1,
                    "createDate": "createDate",
                    "supplyDate": "supplyDate",
                    "factDate": "factDate",
                    "updatedDate": "updatedDate",
                    "statusID": 1,
                    "boxTypeID": None,
                    "isBoxOnPallet": True,
                }
            ]
        )

        result = await api.get_supplies_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SuppliesListResponse)
        assert result[0].phone == "phone"
        assert result[0].supply_id == 1
        assert result[0].preorder_id == 1
        assert result[0].create_date == "createDate"
        assert result[0].supply_date == "supplyDate"
