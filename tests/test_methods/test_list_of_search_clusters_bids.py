import pytest

from wbapi_async.types.list_of_search_clusters_bids_item import ListOfSearchClustersBidsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestListOfSearchClustersBids:

    async def test_list_of_search_clusters_bids(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "bids": [{
                "advert_id": 1,
                "nm_id": 1,
                "norm_query": "norm_query",
                "bid": 1,
            }]
        }
        )

        result = await api.list_of_search_clusters_bids(items=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfSearchClustersBidsItem)
        assert result[0].advert_id == 1
        assert result[0].nm_id == 1
        assert result[0].norm_query == "norm_query"
