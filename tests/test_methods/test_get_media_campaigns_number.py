import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import MediaCampaignsNumberResponse


@pytest.mark.unit
class TestGetMediaCampaignsNumber:
    async def test_get_media_campaigns_number(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "all": 1,
                    "adverts": {"type": 1, "status": 1, "count": 1},
                }
            ]
        )

        result = await api.get_media_campaigns_number()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], MediaCampaignsNumberResponse)
        assert result[0].all_ == 1
