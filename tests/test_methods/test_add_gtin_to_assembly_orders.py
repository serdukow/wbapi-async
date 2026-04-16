import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AddGtinToAssemblyOrdersItem


@pytest.mark.unit
class TestAddGtinToAssemblyOrders:
    async def test_add_gtin_to_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "results": [
                    {
                        "errors": [{"code": 404, "detail": "NotFound"}],
                        "isError": True,
                        "orderId": 123456,
                    }
                ]
            }
        )

        result = await api.add_gtin_to_assembly_orders(orders=[{"gtin": "1234567890123", "orderId": 123456}])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AddGtinToAssemblyOrdersItem)
        assert result[0].is_error
        assert result[0].order_id == 123456
