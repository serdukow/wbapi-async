import pytest

from wbapi_async.types.media_campaigns_number_response import MediaCampaignsNumberResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetMediaCampaignsNumber:

    async def test_get_media_campaigns_number(self, api: MockedAPI) -> None:
        api.add_response(
            [{
                "all": 1,
                "adverts": {},
            }]
        )

        result = await api.get_media_campaigns_number()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], MediaCampaignsNumberResponse)
        assert result[0].all == 1
        assert result[0].adverts == {}
