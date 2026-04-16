import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import NotifyThatTheOrdersAreReceivedItem


@pytest.mark.unit
class TestNotifyThatTheOrdersAreReceived:
    async def test_notify_that_the_orders_are_received(self, api: MockedAPI) -> None:
        api.add_response(
            {
                "results": [
                    {
                        "errors": [{"code": 1, "detail": "detail"}],
                        "isError": True,
                        "orderId": 123456,
                    }
                ]
            }
        )

        result = await api.notify_that_the_orders_are_received(orders=[{"code": "741852", "orderId": 123456}])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NotifyThatTheOrdersAreReceivedItem)
        assert result[0].is_error
        assert result[0].order_id == 123456
