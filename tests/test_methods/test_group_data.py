import pytest

from wbapi_async.types.group_data_item import GroupDataItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGroupData:

    async def test_group_data(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "data": {
            "groups": [{
                "subjectID": 1,
                "subjectName": "subjectName",
                "brandName": "brandName",
                "tagID": 1,
                "tagName": "tagName",
                "metrics": None,
                "items": [],
            }]
        }
        }
        )

        result = await api.group_data()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], GroupDataItem)
        assert result[0].subject_id == 1
        assert result[0].subject_name == "subjectName"
        assert result[0].brand_name == "brandName"
