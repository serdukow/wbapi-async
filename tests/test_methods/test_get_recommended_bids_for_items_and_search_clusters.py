import pytest

from wbapi_async.types import RecommendedBidsForItemsAndSearchClustersItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetRecommendedBidsForItemsAndSearchClusters:

    async def test_get_recommended_bids_for_items_and_search_clusters(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "normQueries": [{
                "normQuery": "normQuery",
                "reachMax": {},
                "reachMedium": {},
                "reachMin": {},
            }]
        }
        )

        result = await api.get_recommended_bids_for_items_and_search_clusters(nm_id=1, advert_id=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], RecommendedBidsForItemsAndSearchClustersItem)
        assert result[0].norm_query == "normQuery"
        assert result[0].reach_max == {}
        assert result[0].reach_medium == {}
