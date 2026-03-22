import pytest

from wbapi_async.types.daily_search_clusters_statistics_item import DailySearchClustersStatisticsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDailySearchClustersStatistics:

    async def test_daily_search_clusters_statistics(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "items": [{
                "advertId": 1,
                "nmId": 1,
                "dailyStats": [],
            }]
        }
        )

        result = await api.daily_search_clusters_statistics(from_="from_", to="to", items=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DailySearchClustersStatisticsItem)
        assert result[0].advert_id == 1
        assert result[0].nm_id == 1
        assert result[0].daily_stats == []
