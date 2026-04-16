import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import PaginationByProductsWithinAGroupResponse


@pytest.mark.unit
class TestGetPaginationByProductsWithinAGroup:
    async def test_get_pagination_by_products_within_a_group(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                }
            ]
        )

        result = await api.get_pagination_by_products_within_a_group(
            current_period={}, order_by={}, position_cluster="position_cluster", limit=1, offset=1
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], PaginationByProductsWithinAGroupResponse)
