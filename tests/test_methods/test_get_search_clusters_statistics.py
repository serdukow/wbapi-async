import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SearchClustersStatisticsItem


@pytest.mark.unit
class TestGetSearchClustersStatistics:
    async def test_get_search_clusters_statistics(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "stats": [
                    {
                        "advert_id": 1,
                        "nm_id": 1,
                        "stats": [
                            {
                                "norm_query": "norm_query",
                                "views": 1,
                                "clicks": 1,
                                "atbs": 1,
                                "orders": 1,
                                "ctr": 1.0,
                                "cpc": 1.0,
                                "cpm": 1.0,
                                "avg_pos": 1.0,
                                "shks": 1,
                                "spend": 1.0,
                            }
                        ],
                    }
                ]
            }
        )

        result = await api.get_search_clusters_statistics(
            from_="from_", to="to", items=[{"advert_id": 1, "nm_id": 1}]
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SearchClustersStatisticsItem)
        assert result[0].advert_id == 1
        assert result[0].nm_id == 1
