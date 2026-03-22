import pytest

from wbapi_async.types.media_campaign_statistics_response import MediaCampaignStatisticsResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestMediaCampaignStatistics:

    async def test_media_campaign_statistics(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.media_campaign_statistics()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], MediaCampaignStatisticsResponse)
