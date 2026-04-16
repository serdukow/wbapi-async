import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import DailySearchClustersStatisticsItem


@pytest.mark.unit
class TestGetDailySearchClustersStatistics:
    async def test_get_daily_search_clusters_statistics(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "items": [
                    {
                        "advertId": 1,
                        "nmId": 1,
                        "dailyStats": [
                            {
                                "date": "date",
                                "stat": {
                                    "normQuery": "normQuery",
                                    "views": 1,
                                    "clicks": 1,
                                    "atbs": 1,
                                    "orders": 1,
                                    "ctr": 1.0,
                                    "cpc": 1.0,
                                    "cpm": 1.0,
                                    "avgPos": 1.0,
                                    "shks": 1,
                                    "spend": 1.0,
                                },
                            }
                        ],
                    }
                ]
            }
        )

        result = await api.get_daily_search_clusters_statistics(
            from_="from_", to="to", items=[{"advertId": 1, "nmId": 1}]
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], DailySearchClustersStatisticsItem)
        assert result[0].advert_id == 1
        assert result[0].nm_id == 1
