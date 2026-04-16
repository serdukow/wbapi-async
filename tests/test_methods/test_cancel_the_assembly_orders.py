import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import CancelTheAssemblyOrdersItem


@pytest.mark.unit
class TestCancelTheAssemblyOrders:
    async def test_cancel_the_assembly_orders(self, api: MockedAPI) -> None:
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

        result = await api.cancel_the_assembly_orders()

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], CancelTheAssemblyOrdersItem)
        assert result[0].order_id == 123456
        assert result[0].is_error
