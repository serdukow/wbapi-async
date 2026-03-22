import pytest

from wbapi_async.types import SearchTextsByProductResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestSearchTextsByProduct:

    async def test_search_texts_by_product(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.search_texts_by_product(current_period={}, nm_ids=[], top_order_by="openCard", order_by={}, limit=None)

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SearchTextsByProductResponse)
