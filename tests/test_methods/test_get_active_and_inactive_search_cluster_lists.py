import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import ActiveAndInactiveSearchClusterListsItem


@pytest.mark.unit
class TestGetActiveAndInactiveSearchClusterLists:
    async def test_get_active_and_inactive_search_cluster_lists(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "items": [
                    {
                        "advertId": 1,
                        "nmId": 1,
                        "normQueries": {"active": [], "excluded": []},
                    }
                ]
            }
        )

        result = await api.get_active_and_inactive_search_cluster_lists(items=[{"advertId": 1, "nmId": 1}])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], ActiveAndInactiveSearchClusterListsItem)
        assert result[0].advert_id == 1
        assert result[0].nm_id == 1
