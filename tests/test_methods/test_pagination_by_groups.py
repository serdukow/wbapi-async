import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import PaginationByGroupsResponse


@pytest.mark.unit
class TestPaginationByGroups:
    async def test_pagination_by_groups(self, api: MockedAPI) -> None:
        api.add_response([{}])

        result = await api.pagination_by_groups(
            current_period={}, order_by={}, position_cluster="all", limit=1, offset=1
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PaginationByGroupsResponse)
