import pytest

from wbapi_async.types.orders_and_positions_by_product_search_texts_response import OrdersAndPositionsByProductSearchTextsResponse
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestOrdersAndPositionsByProductSearchTexts:

    async def test_orders_and_positions_by_product_search_texts(self, api: MockedAPI) -> None:
        api.add_response(
            [{

            }]
        )

        result = await api.orders_and_positions_by_product_search_texts(period={}, nm_id=1, search_texts=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OrdersAndPositionsByProductSearchTextsResponse)
