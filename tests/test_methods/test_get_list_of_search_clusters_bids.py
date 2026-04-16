import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ListOfSearchClustersBidsItem


@pytest.mark.unit
class TestGetListOfSearchClustersBids:
    async def test_get_list_of_search_clusters_bids(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "bids": [
                    {
                        "advert_id": 1,
                        "nm_id": 1,
                        "norm_query": "norm_query",
                        "bid": 1,
                    }
                ]
            }
        )

        result = await api.get_list_of_search_clusters_bids(items=[{"advert_id": 1, "nm_id": 1}])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ListOfSearchClustersBidsItem)
        assert result[0].advert_id == 1
        assert result[0].nm_id == 1
        assert result[0].norm_query == "norm_query"
        assert result[0].bid == 1
