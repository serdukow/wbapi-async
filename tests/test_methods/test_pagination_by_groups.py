import pytest

from wbapi_async.types.pagination_by_groups_response import PaginationByGroupsResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestPaginationByGroups:

    async def test_pagination_by_groups(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.pagination_by_groups(current_period={}, order_by={}, position_cluster="position_cluster", limit=1, offset=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PaginationByGroupsResponse)
