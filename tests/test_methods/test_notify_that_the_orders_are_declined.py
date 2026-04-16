import pytest

from tests.mocked_api import MockedAPI
from wbapi_async.types import NotifyThatTheOrdersAreDeclinedItem


@pytest.mark.unit
class TestNotifyThatTheOrdersAreDeclined:
    async def test_notify_that_the_orders_are_declined(self, api: MockedAPI) -> None:
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

        result = await api.notify_that_the_orders_are_declined(orders=[{"code": "741852", "orderId": 123456}])

        assert isinstance(result, list)
        assert len(result) == 1
        assert isinstance(result[0], NotifyThatTheOrdersAreDeclinedItem)
        assert result[0].is_error
        assert result[0].order_id == 123456
