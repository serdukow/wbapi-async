import pytest

from wbapi_async.types import CancelAssemblyOrdersItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestCancelAssemblyOrders:

    async def test_cancel_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "results": [{
                "errors": [],
                "isError": True,
                "orderId": 1,
            }]
        }
        )

        result = await api.cancel_assembly_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CancelAssemblyOrdersItem)
        assert result[0].errors == []
        assert result[0].is_error == True
        assert result[0].order_id == 1
