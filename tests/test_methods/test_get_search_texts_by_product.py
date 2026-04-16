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
            current_period={"start": "2023-06-01", "end": "2024-03-01"},
            nm_ids=[],
            top_order_by="top_order_by",
            order_by={"field": "openCard", "mode": "mode"},
            limit=None,
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], SearchTextsByProductResponse)
