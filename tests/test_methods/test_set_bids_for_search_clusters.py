import pytest

from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestSetBidsForSearchClusters:

    async def test_set_bids_for_search_clusters(self, api: MockedAPI) -> None:
        api.add_response(
            None
        )

        result = await api.set_bids_for_search_clusters(bids=[])

        assert result is None
