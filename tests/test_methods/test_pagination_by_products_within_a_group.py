import pytest

from wbapi_async.types.pagination_by_products_within_a_group_response import PaginationByProductsWithinAGroupResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestPaginationByProductsWithinAGroup:

    async def test_pagination_by_products_within_a_group(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.pagination_by_products_within_a_group(current_period={}, order_by={}, position_cluster="position_cluster", limit=1, offset=1)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PaginationByProductsWithinAGroupResponse)
