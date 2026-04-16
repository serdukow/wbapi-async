import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CampaignsListsItem


@pytest.mark.unit
class TestGetCampaignsLists:
    async def test_get_campaigns_lists(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "adverts": [
                    {
                        "type": 1,
                        "status": 1,
                        "count": 1,
                        "advert_list": [{"advertId": 1, "changeTime": "changeTime"}],
                    }
                ]
            }
        )

        result = await api.get_campaigns_lists()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CampaignsListsItem)
        assert result[0].type_ == 1
        assert result[0].status == 1
        assert result[0].count == 1
