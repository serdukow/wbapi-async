import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CancelAssemblyOrdersItem


@pytest.mark.unit
class TestCancelAssemblyOrders:
    async def test_cancel_assembly_orders(self, api: MockedAPI) -> None:
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

        result = await api.cancel_assembly_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CancelAssemblyOrdersItem)
        assert result[0].is_error
        assert result[0].order_id == 123456
