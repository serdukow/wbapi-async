import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestDeleteBidsFromSearchClusters:
    async def test_delete_bids_from_search_clusters(self, api: MockedAPI) -> None:
        api.add_response(None)

        result = await api.delete_bids_from_search_clusters(bids=[])

        assert result is None
