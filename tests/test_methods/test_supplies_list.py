import pytest

from wbapi_async.types.supplies_list_response import SuppliesListResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestSuppliesList:

    async def test_supplies_list(self, api: MockedAPI) -> None:
        api.add_response(
            [{
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
            }]
        )

        result = await api.supplies_list()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SuppliesListResponse)
        assert result[0].phone == "phone"
        assert result[0].supply_id == 1
        assert result[0].preorder_id == 1
