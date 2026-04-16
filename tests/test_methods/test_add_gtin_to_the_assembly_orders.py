import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AddGtinToTheAssemblyOrdersItem


@pytest.mark.unit
class TestAddGtinToTheAssemblyOrders:
    async def test_add_gtin_to_the_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "results": [
                    {
                        "orderId": 123456,
                        "isError": True,
                        "errors": [{"code": 404, "detail": "NotFound"}],
                    }
                ]
            }
        )

        result = await api.add_gtin_to_the_assembly_orders(
            orders=[{"gtin": "1234567890123", "orderId": 123456}]
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AddGtinToTheAssemblyOrdersItem)
        assert result[0].order_id == 123456
        assert result[0].is_error
