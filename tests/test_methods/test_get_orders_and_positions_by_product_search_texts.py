import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import OrdersAndPositionsByProductSearchTextsResponse


@pytest.mark.unit
class TestGetOrdersAndPositionsByProductSearchTexts:
    async def test_get_orders_and_positions_by_product_search_texts(self, api: MockedAPI) -> None:
        api.add_response(
            [
                {
                    "data": {},
                }
            ]
        )

        result = await api.get_orders_and_positions_by_product_search_texts(
            period={"start": "2023-06-01", "end": "2024-03-01"}, nm_id=1, search_texts=[]
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OrdersAndPositionsByProductSearchTextsResponse)
