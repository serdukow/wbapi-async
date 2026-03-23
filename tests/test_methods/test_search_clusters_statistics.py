import pytest

from wbapi_async.types import SearchClustersStatisticsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestSearchClustersStatistics:

    async def test_search_clusters_statistics(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "stats": [{
                "advert_id": 1,
                "nm_id": 1,
                "stats": [],
            }]
        }
        )

        result = await api.search_clusters_statistics(from_="from_", to="to", items=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SearchClustersStatisticsItem)
        assert result[0].advert_id == 1
        assert result[0].nm_id == 1
        assert result[0].stats == []
