import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AddImeiToAssemblyOrdersItem


@pytest.mark.unit
class TestAddImeiToAssemblyOrders:
    async def test_add_imei_to_assembly_orders(self, api: MockedAPI) -> None:
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

        result = await api.add_imei_to_assembly_orders(
            orders=[{"orderId": 123456, "imei": "654321741987258"}]
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AddImeiToAssemblyOrdersItem)
        assert result[0].is_error
        assert result[0].order_id == 123456
