import pytest

from wbapi_async.types.active_and_inactive_search_cluster_lists_item import ActiveAndInactiveSearchClusterListsItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestActiveAndInactiveSearchClusterLists:

    async def test_active_and_inactive_search_cluster_lists(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "items": [{
                "advertId": 1,
                "nmId": 1,
                "normQueries": {},
            }]
        }
        )

        result = await api.active_and_inactive_search_cluster_lists(items=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ActiveAndInactiveSearchClusterListsItem)
        assert result[0].advert_id == 1
        assert result[0].nm_id == 1
        assert result[0].norm_queries == {}
