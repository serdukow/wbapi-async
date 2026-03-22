import pytest

from wbapi_async.types import ListOfMediaCampaignsResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetListOfMediaCampaigns:

    async def test_get_list_of_media_campaigns(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "advertId": 1,
                "name": "name",
                "brand": "brand",
                "type": 1,
                "status": 1,
                "createTime": "createTime",
                "endTime": "endTime",
            }]
        )

        result = await api.get_list_of_media_campaigns()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfMediaCampaignsResponse)
        assert result[0].advert_id == 1
        assert result[0].name == "name"
        assert result[0].brand == "brand"
