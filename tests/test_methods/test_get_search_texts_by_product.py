import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import SearchTextsByProductResponse


@pytest.mark.unit
class TestGetSearchTextsByProduct:
    async def test_get_search_texts_by_product(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                }
            ]
        )

        result = await api.get_search_texts_by_product(
            current_period={"start": "2024-02-10", "end": "2024-02-10"},
            nm_ids=[],
            top_order_by="openCard",
            order_by={"field": "openCard", "mode": "asc"},
            limit=None,
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SearchTextsByProductResponse)
