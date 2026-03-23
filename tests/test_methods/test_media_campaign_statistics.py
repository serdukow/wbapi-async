import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import MediaCampaignStatisticsResponse


@pytest.mark.unit
class TestMediaCampaignStatistics:
    async def test_media_campaign_statistics(self, api: MockedAPI) -> None:
        api.add_response([{}])

        result = await api.media_campaign_statistics()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], MediaCampaignStatisticsResponse)
