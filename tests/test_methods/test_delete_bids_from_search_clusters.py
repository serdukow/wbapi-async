import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDeleteBidsFromSearchClusters:
    async def test_delete_bids_from_search_clusters(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.delete_bids_from_search_clusters(
            bids=[{"advert_id": 1, "nm_id": 1, "norm_query": "norm_query", "bid": 1}]
        )

        assert result is None
