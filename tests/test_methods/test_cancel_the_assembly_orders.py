import pytest

from wbapi_async.types import CancelTheAssemblyOrdersItem
from tests.mocked_api import MockedAPI


@pytest.mark.unit
class TestCancelTheAssemblyOrders:

    async def test_cancel_the_assembly_orders(self, api: MockedAPI) -> None:
        api.add_response(
            {
            "results": [{
                "orderId": 1,
                "isError": True,
                "errors": [],
            }]
        }
        )

        result = await api.cancel_the_assembly_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CancelTheAssemblyOrdersItem)
        assert result[0].order_id == 1
        assert result[0].is_error == True
        assert result[0].errors == []
