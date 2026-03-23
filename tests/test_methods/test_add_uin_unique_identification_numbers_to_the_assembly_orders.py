import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem


@pytest.mark.unit
class TestAddUinUniqueIdentificationNumbersToTheAssemblyOrders:
    async def test_add_uin_unique_identification_numbers_to_the_assembly_orders(self, api: MockedAPI) -> None:
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

        result = await api.add_uin_unique_identification_numbers_to_the_assembly_orders(orders=[])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AddUinUniqueIdentificationNumbersToTheAssemblyOrdersItem)
        assert result[0].order_id == 1
        assert result[0].is_error
        assert result[0].errors == []
