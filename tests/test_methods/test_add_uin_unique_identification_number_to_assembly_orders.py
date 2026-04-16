import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import AddUinUniqueIdentificationNumberToAssemblyOrdersItem


@pytest.mark.unit
class TestAddUinUniqueIdentificationNumberToAssemblyOrders:
    async def test_add_uin_unique_identification_number_to_assembly_orders(self, api: MockedAPI) -> None:
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

        result = await api.add_uin_unique_identification_number_to_assembly_orders(
            orders=[{"orderId": 123456, "uin": "1234568909091232"}]
        )

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], AddUinUniqueIdentificationNumberToAssemblyOrdersItem)
        assert result[0].is_error
        assert result[0].order_id == 123456
