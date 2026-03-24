import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AddImeiToTheAssemblyOrdersItem


@pytest.mark.unit
class TestAddImeiToTheAssemblyOrders:
    async def test_add_imei_to_the_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "results": [
                    {
                        "orderId": 1,
                        "isError": True,
                        "errors": [],
                    }
                ]
            }
        )

        result = await api.add_imei_to_the_assembly_orders(orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AddImeiToTheAssemblyOrdersItem)
        assert result[0].order_id == 1
        assert result[0].is_error
        assert result[0].errors == []
