import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SizeDataItem


@pytest.mark.unit
class TestSizeData:
    async def test_size_data(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "data": {
                    "offices": [
                        {
                            "regionName": "regionName",
                            "officeID": 1,
                            "officeName": "officeName",
                            "metrics": None,
                        }
                    ]
                }
            }
        )

        result = await api.size_data()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SizeDataItem)
        assert result[0].region_name == "regionName"
        assert result[0].office_id == 1
        assert result[0].office_name == "officeName"
