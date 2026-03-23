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
                        "errors": [],
                        "isError": True,
                        "orderId": 1,
                    }
                ]
            }
        )

        result = await api.add_imei_to_assembly_orders(orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AddImeiToAssemblyOrdersItem)
        assert result[0].errors == []
        assert result[0].is_error
        assert result[0].order_id == 1
