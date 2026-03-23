import pytest

from wbapi_async.types import OrdersStickersItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestGetOrdersStickers:

    async def test_get_orders_stickers(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "stickers": [{
                "orderId": 1,
                "partA": "partA",
                "partB": "partB",
                "barcode": "barcode",
                "file": "file",
            }]
        }
        )

        result = await api.get_orders_stickers(type_="svg", width="58", height="40")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], OrdersStickersItem)
        assert result[0].order_id == 1
        assert result[0].part_a == "partA"
        assert result[0].part_b == "partB"
