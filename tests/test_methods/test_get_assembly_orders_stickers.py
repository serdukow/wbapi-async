import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AssemblyOrdersStickersItem


@pytest.mark.unit
class TestGetAssemblyOrdersStickers:
    async def test_get_assembly_orders_stickers(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "stickers": [
                    {
                        "orderId": 1,
                        "partA": 1,
                        "partB": 1,
                        "barcode": "barcode",
                        "file": "file",
                    }
                ]
            }
        )

        result = await api.get_assembly_orders_stickers(type="svg", width="58", height="40")

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AssemblyOrdersStickersItem)
        assert result[0].order_id == 1
        assert result[0].part_a == 1
        assert result[0].part_b == 1
